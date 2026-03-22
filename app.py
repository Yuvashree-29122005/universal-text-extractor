import streamlit as st
from image_ocr import extract_text_from_image
from pdf_ocr import extract_text_from_pdf
from PIL import Image
import tempfile

st.title("Universal Text Extractor")

file = st.file_uploader("Upload Image or PDF")

if file:
    file_type = file.type

    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        tmp.write(file.read())
        temp_path = tmp.name

    if "image" in file_type:
        text = extract_text_from_image(temp_path)

    elif "pdf" in file_type:
        text = extract_text_from_pdf(temp_path)

    st.text_area("Extracted Text", text, height=300)