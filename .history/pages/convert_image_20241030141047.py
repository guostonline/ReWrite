

import streamlit as st
from PIL import Image
import os

def convert_to_webp(input_image):
    output_file = os.path.splitext(input_image.name)[0] + ".webp"
    input_image.save(output_file, "WebP")
    return output_file

st.title("Image to WebP Converter")
uploaded_file = st.file_uploader("Choose an image file", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Original Image', use_column_width=True)

    webp_file = convert_to_webp(uploaded_file)
    st.download_button(
        label="Download WebP Image",
        data=open(webp_file, "rb").read(),
        file_name=webp_file,
        mime="image/webp",
    )