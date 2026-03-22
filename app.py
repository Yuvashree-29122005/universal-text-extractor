import streamlit as st
from image_ocr import extract_text_from_image
from pdf_ocr import extract_text_from_pdf
import tempfile

st.set_page_config(page_title="Universal Text Extractor", page_icon="📄")

st.title("📄 Universal Text Extractor")
st.write("Upload Image or PDF and extract text instantly 🔥")

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

    st.subheader("📜 Extracted Text")

    # TEXT AREA
    st.text_area("Output", text, height=300)

    # COPY BUTTON
    st.code(text, language="text")

    # DOWNLOAD BUTTON
    st.download_button(
        label="⬇️ Download Text",
        data=text,
        file_name="extracted_text.txt",
        mime="text/plain"
    )
