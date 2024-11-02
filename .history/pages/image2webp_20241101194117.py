import streamlit as st
from PIL import Image
import os

# Preset sizes dictionary (width x height in pixels)
PRESET_SIZES = {
    "WordPress Post":(1200,675),
    "Custom Size": None,
    "Instagram Square Post": (1080, 1080),
    "Instagram Portrait": (1080, 1350),
    "Instagram Story": (1080, 1920),
    "Facebook Cover": (851, 315),
    "Facebook Post": (1200, 630),
    "Twitter Header": (1500, 500),
    "Twitter Post": (1200, 675),
    "LinkedIn Cover": (1584, 396),
    "LinkedIn Post": (1200, 627),
    "YouTube Thumbnail": (1280, 720),
    "YouTube Channel Art": (2560, 1440),
}

def resize_image(image, size):
    """Resize image while maintaining aspect ratio"""
    if size:
        image.thumbnail(size, Image.Resampling.LANCZOS)
    return image

def convert_to_webp(input_image, size=None, quality=90):
    """Convert image to WebP format with optional resizing"""
    output_file = os.path.splitext(input_image.name)[0] + ".webp"
    image = Image.open(input_image)
    
    # Resize if size is specified
    if size:
        image = resize_image(image, size)
    
    # Save as WebP
    image.save(output_file, "WebP", quality=quality)
    return output_file, image

def main():
    st.set_page_config(page_title="Advanced Image Converter", layout="wide")
    st.title("Advanced Image to WebP Converter")
    
    # File uploader
    uploaded_file = st.file_uploader("Choose an image file", type=["jpg", "jpeg", "png"])
    
    if uploaded_file is not None:
        # Show original image
        original_image = Image.open(uploaded_file)
        st.subheader("Original Image")
        st.image(original_image, caption=f"Original Size: {original_image.size[0]}x{original_image.size[1]} pixels")
        
        # Create two columns for options
        col1, col2 = st.columns(2)
        
        with col1:
            # Preset format selector
            selected_preset = st.selectbox("Select Format", list(PRESET_SIZES.keys()))
            
        with col2:
            # Quality slider
            quality = st.slider("WebP Quality", min_value=1, max_value=100, value=90)
            
        # Custom size inputs if "Custom Size" is selected
        if selected_preset == "Custom Size":
            custom_col1, custom_col2 = st.columns(2)
            with custom_col1:
                custom_width = st.number_input("Width (pixels)", min_value=1, value=original_image.size[0])
            with custom_col2:
                custom_height = st.number_input("Height (pixels)", min_value=1, value=original_image.size[1])
            size = (custom_width, custom_height)
        else:
            size = PRESET_SIZES[selected_preset]
        
        # Convert button
        if st.button("Convert to WebP"):
            webp_file, converted_image = convert_to_webp(uploaded_file, size, quality)
            
            # Display converted image
            st.subheader("Converted Image")
            st.image(converted_image, caption=f"Converted Size: {converted_image.size[0]}x{converted_image.size[1]} pixels")
            
            # Download button
            with open(webp_file, "rb") as file:
                st.download_button(
                    label="Download WebP Image",
                    data=file,
                    file_name=os.path.basename(webp_file),
                    mime="image/webp",
                )
            
            # Show conversion details
            st.success(f"""
            Conversion successful!
            - Original size: {original_image.size[0]}x{original_image.size[1]} pixels
            - Converted size: {converted_image.size[0]}x{converted_image.size[1]} pixels
            - Quality: {quality}%
            """)

if __name__ == "__main__":
    main()