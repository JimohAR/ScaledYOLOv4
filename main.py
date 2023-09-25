import streamlit as st
import glob
import os


st.markdown(""" # Gun Detection Model """)

uploaded_file = st.file_uploader(
    "Upload Image", accept_multiple_files=False, type=["jpg"]
)

if uploaded_file:
    # for uploaded_file in uploaded_files:
    with open("inference/images/" + uploaded_file.name, "wb") as f:
        f.write(uploaded_file.getvalue())


if uploaded_file:
    run = st.button("RUN")
    if run:
        # python detect
        os.system("python detect.py --img 416")

        images = []
        for imageName in glob.glob("inference/output/*.jp*"):  # assuming JPG, JPEG
            with open(imageName, "rb") as f:
                images.append(f.read())

        st.image(image=images)

        for f in glob.glob("./inference/*/*.*"):
            os.remove(f)
