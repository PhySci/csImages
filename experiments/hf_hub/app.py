import streamlit as st
from PIL import Image
import base64
import requests
from io import BytesIO
import os

col1, col2 = st.columns(2)

with col1:
    orig_file = st.file_uploader("Choose an original image", type="jpg")
    prompt = st.text_area(label="prompt",
                          value="Vibrant, cartoon-style cat astronaut, perfect for slot game art.")
    negative_prompt = st.text_area(label="negative prompt",
                                   value="Vibrant, cartoon-style cat astronaut, perfect for slot game art.")
    strength = st.slider(label="strength",
                         min_value=0.05,
                         max_value=1.0)

if orig_file is not None:
    with col2:
        payload = {"inputs":
                       {"image": base64.b64encode(orig_file.getvalue()).decode("utf8"),
                        "strength": strength,
                        "prompt": prompt,
                        "negative_prompt": negative_prompt}
                   }
        API_URL = "https://juwk62dxv3rfpdxn.us-east-1.aws.endpoints.huggingface.cloud"
        headers = {
            "Accept": "application/json",
            "Authorization": os.environ["HF_TOKEN"],
            "Content-Type": "application/json"
        }
        response = requests.post(API_URL, headers=headers, json=payload)
        if response.status_code != 200:
            st.write(response.text)
        else:
            js = response.json()
            img = Image.open(BytesIO(base64.b64decode(js["image"])))
            st.image(img)