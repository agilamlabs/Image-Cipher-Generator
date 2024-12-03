#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 18:05:59 2024

@author: gn
"""

import streamlit as st
import numpy as np
from PIL import Image
import io

# Function to apply a simple cipher to the image
def cipher_image(image, shift_value=50):
    # Convert image to numpy array
    img_array = np.array(image)

    # Apply a simple cipher (e.g., shift RGB values)
    img_array = (img_array + shift_value) % 256

    # Convert back to image
    ciphered_image = Image.fromarray(img_array.astype('uint8'))
    return ciphered_image

# Function to decipher the image
def decipher_image(image, shift_value=50):
    # Convert image to numpy array
    img_array = np.array(image)

    # Apply a simple decipher (reverse the shift)
    img_array = (img_array - shift_value) % 256

    # Convert back to image
    deciphered_image = Image.fromarray(img_array.astype('uint8'))
    return deciphered_image

# Streamlit interface
st.title("Image Cipher Generator")

# Adding LinkedIn link and creator information
st.markdown("""
<div style="display: flex; align-items: center; background-color: black; padding: 5px; border-radius: 3px;">
    <span style="font-size: 18px; color: #2e8b57; font-weight: bold; margin-right: 10px;">Created by:</span>
    <a href="https://www.linkedin.com/in/gn-raavanan" target="_blank" style="text-decoration: none; display: flex; align-items: center;">
        <img src="https://upload.wikimedia.org/wikipedia/commons/c/ca/LinkedIn_logo_initials.png" alt="LinkedIn" style="width: 20px; height: 20px; margin-right: 5px;">
        <span style="font-size: 18px; font-weight: bold; color: #fff;">Gokul nath</span>
    </a>
</div>
""", unsafe_allow_html=True)


st.write("#### Upload an image to apply a cipher or decipher it.")

# Image upload
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Load the uploaded image
    image = Image.open(uploaded_file)

    # Display the original image
    st.image(image, caption='Original Image', use_column_width=True)

    # Shift value for ciphering/deciphering
    shift_value = st.slider("Shift Value", min_value=1, max_value=255, value=50)

    # Option to apply cipher or decipher
    action = st.selectbox("Choose action", ["Cipher", "Decipher"])

    if action == "Cipher":
        # Apply cipher to the image
        processed_image = cipher_image(image, shift_value)
        st.image(processed_image, caption='Ciphered Image', use_column_width=True)
        file_name = "ciphered_image.png"
    else:
        # Apply decipher to the image
        processed_image = decipher_image(image, shift_value)
        st.image(processed_image, caption='Deciphered Image', use_column_width=True)
        file_name = "deciphered_image.png"

    # Save the processed image to a buffer
    buf = io.BytesIO()
    processed_image.save(buf, format="PNG")
    byte_im = buf.getvalue()

    # Option to download the processed image
    st.download_button(label=f"Download {action}ed Image",
                       data=byte_im,
                       file_name=file_name,
                       mime="image/png")
