import os
os.system("pip install git+https://github.com/facebookresearch/detectron2.git")

import streamlit as st
import cv2
import numpy as np
from detectron2.utils.visualizer import Visualizer, ColorMode
from detectron2.data import MetadataCatalog
import cv2
import gdown
from detectron2.data import DatasetCatalog, MetadataCatalog
from detectron2.utils.visualizer import Visualizer
from detectron2.utils.visualizer import ColorMode
from detectron2 import model_zoo
from detectron2.config import get_cfg
from detectron2.engine import DefaultPredictor
from detectron2.config import get_cfg
import os

st.title("Object Detection on Cars")
st.markdown("""
Upload an image, and the system will detect objects using two models:
- **RetinaNet**
- **Faster-RCNN**
Results will be displayed side by side for comparison.
""")

@st.cache_resource
def download_model():
    gdown.download_folder("https://drive.google.com/drive/folders/1o08O30SP23uskXhIHZuQxXSNeEzbUcHh?usp=sharing", remaining_ok=True)
    gdown.download_folder("https://drive.google.com/drive/folders/1Zenq1klMwcDvPXblZ2au92vm7L8KE8se?usp=sharing", remaining_ok=True)

download_model()

@st.cache_resource
def createMetadata():
    dataset_dicts = []
    # Misalnya, membuat 10 gambar palsu dengan anotasi palsu
    for idx in range(10):
        record = {
            "file_name": f"image_{idx}.jpg",  # Nama file gambar
            "image_id": idx,  # ID gambar
            "height": 480,
            "width": 640,
            "annotations": [
                {
                    "bbox": [np.random.randint(0, 500), np.random.randint(0, 400), 100, 100],  # Bbox acak
                    "bbox_mode": 0,  # Deteksi bounding box mode
                    "category_id": 0,  # ID kategori (0 untuk car)
                    "iscrowd": 0,
                }
            ]
        }
        dataset_dicts.append(record)
    DatasetCatalog.register("custom_train", dataset_dicts)


metadata = MetadataCatalog.get("custom_train").set(
    thing_classes=["car"],
)


@st.cache_resource
def loadPredictor(model_path, model_name):
    cfg = get_cfg()
    cfg.merge_from_file(model_zoo.get_config_file(f"COCO-Detection/{model_name}.yaml"))
    cfg.MODEL.WEIGHTS = os.path.join(model_path, "model_final.pth")

    cfg.DATALOADER.NUM_WORKERS = 4
    cfg.MODEL.ROI_HEADS.BATCH_SIZE_PER_IMAGE = 64
    cfg.MODEL.ROI_HEADS.NUM_CLASSES = 1 #your number of classes + 1
    cfg.MODEL.RETINANET.NUM_CLASSES = 1
    cfg.MODEL.DEVICE = 'cpu'


    predictor = DefaultPredictor(cfg)
    return predictor

retina_model=loadPredictor("retinanet_R_101_FPN_3x","retinanet_R_101_FPN_3x")
fasterrcnn_model=loadPredictor("faster_rcnn_R_101_FPN_3x","faster_rcnn_R_101_FPN_3x")

def inference(img, model):
    outputs = model(img)

    instances = outputs["instances"].to("cpu")
    if len(instances) > 0:
        scores = instances.scores
        instances = instances[scores > 0.6]

    # Visualization
    pred_visualizer = Visualizer(
        img,
        metadata=metadata,
        scale=0.8,
        instance_mode=ColorMode.IMAGE
    )
    out_pred = pred_visualizer.draw_instance_predictions(instances).get_image()
    return out_pred

# Image Upload
uploaded_file = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    # Load Image
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

    st.image(img[:, :, ::-1], channels="RGB", caption="Uploaded Image", use_container_width=True)

    # Inference with Both Models
    st.subheader("Detection Results")
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### RetinaNet")
        out_pred_retina = inference(img[:, :, ::-1], retina_model)
        st.image(out_pred_retina, channels="RGB", use_container_width=True, caption="RetinaNet Output")

    with col2:
        st.markdown("### Faster-RCNN")
        out_pred_fasterrcnn = inference(img[:, :, ::-1], fasterrcnn_model)
        st.image(out_pred_fasterrcnn, channels="RGB", use_container_width=True, caption="Faster-RCNN Output")

else:
    st.info("Please upload an image to proceed.")