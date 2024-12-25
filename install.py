import os
import subprocess

def install_requirements():
    subprocess.check_call([os.sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])

def install_detectron2():
    subprocess.check_call([os.sys.executable, "-m", "pip", "install", "git+https://github.com/facebookresearch/detectron2.git"])

if __name__ == "__main__":
    install_requirements()  # Install the dependencies first
    install_detectron2()    # Then install detectron2 after
