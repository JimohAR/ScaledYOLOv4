cd ScaledYOLOv4

mkdir inference
mkdir inference/output
mkdir inference/images
cd ..

git clone https://github.com/JunnYu/mish-cuda
cd mish-cuda
python setup.py build install
cd ..

pip install -U PyYAML streamlit pyngrok
