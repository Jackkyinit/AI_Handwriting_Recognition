import streamlit as st
from PIL import Image
import tempfile
from predict_transformer import predict_text

st.title("AI Handwriting Recognition (Transformer)")

uploaded_file = st.file_uploader(
    "Upload handwriting image", type=["png", "jpg", "jpeg"]
)

if uploaded_file is not None:

    image = Image.open(uploaded_file)

    st.image(image, caption="Uploaded Image", width=500)

    with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as tmp:

        image.save(tmp.name)

        text = predict_text(tmp.name)

    st.subheader("Prediction")
    st.write(text)
