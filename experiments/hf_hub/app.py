import streamlit as st
from PIL import Image
import base64
import requests
from io import BytesIO
import os


def transform(img: BytesIO, strength: float, prompt: str, negative_prompt: str) -> [BytesIO, str]:
    payload = {"inputs":
                   {"image": base64.b64encode(img.getvalue()).decode("utf8"),
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
        return None, response.text
    else:
        js = response.json()
        return BytesIO(base64.b64decode(js["image"])), None


def remove_backgroung(img: BytesIO):
    payload = {"inputs": {"image": base64.b64encode(img.getvalue()).decode("utf8")}}
    API_URL = "https://obeur3b3llz2nqkl.us-east-1.aws.endpoints.huggingface.cloud"
    headers = {
        "Accept": "application/json",
        "Authorization": os.environ["HF_TOKEN"],
        "Content-Type": "application/json"
    }
    response = requests.post(API_URL, headers=headers, json=payload)
    if response.status_code != 200:
        return None, response.text
    else:
        js = response.json()
        return BytesIO(base64.b64decode(js["image"])), None


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
        st.image(orig_file)

        img2, response_text = transform(orig_file, strength, prompt, negative_prompt)

        if img2 is None:
            st.write(response_text)
        else:
            st.image(Image.open(img2))

        if img2 is not None:
            img3, response_text = remove_backgroung(img2)

        if img3 is None:
            st.write(response_text)
        else:
            st.image(Image.open(img3))
