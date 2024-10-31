import streamlit as st
from PIL import Image
import os

def convert_to_webp(input_image):
    output_file = os.path.splitext(input_image.name)[0] + ".webp"
    image = Image.open(input_image)
    image.save(output_file, "WebP")
    return output_file

st.set_page_config(page_title="Image to WebP Converter")
st.title("Image to WebP Converter")

uploaded_file = st.file_uploader("Choose an image file", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    webp_file = convert_to_webp(uploaded_file)
    st.success(f"Converted {uploaded_file.name} to {os.path.basename(webp_file)}")
    
    with open(webp_file, "rb") as file:
        st.download_button(
            label="Download WebP Image",
            data=file,
            file_name=os.path.basename(webp_file),
            mime="image/webp",
        )