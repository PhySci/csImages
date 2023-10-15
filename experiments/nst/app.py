import os.path

import streamlit as st
import numpy as np
from nst import main as redraw_image
from PIL import Image
import io

img_list = [("Candy", "candy.jpg"),
            ("Colors","colors.jpg"),
            ("Kandinsky", "kandinsky.jpg"),
            ("Picasso", "picasso.jpg"),
            ("Star nigh", "star_night.jpg")]


for img_name, img_col in zip(img_list, st.columns(len(img_list))):
    with img_col:
        st.write(img_name[0])
        st.image(os.path.join(os.path.dirname(__file__), "style_img", img_name[1]))

genre = st.radio(
    "Choose style image",
    [el[0] for el in img_list])

orig_file = st.file_uploader("Choose an original image", type="jpg")

col1, col2 = st.columns(2)


if orig_file is not None:

    st.write(genre)
    # Convert the file to an opencv image.
    file_bytes = np.asarray(bytearray(orig_file.read()), dtype=np.uint8)

    input_img = Image.open(io.BytesIO(file_bytes))
    input_arr = np.asarray(input_img)


    with col1:
        st.header("Input image")
        st.image(input_img)

    new_img = redraw_image(np.asarray(input_img), genre)

    with col2:
        st.header("New image")
        st.image(new_img)