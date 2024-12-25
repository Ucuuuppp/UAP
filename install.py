import os
import subprocess
import streamlit as st

@st.cache_resource
def install_requirements():
    subprocess.check_call([os.sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])

@st.cache_resource
def install_detectron2():
    subprocess.check_call([os.sys.executable, "-m", "pip", "install", "git+https://github.com/facebookresearch/detectron2.git"])
