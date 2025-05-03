
import streamlit as st
from PIL import Image
from utils.predict import predict_image

st.title("Colonoscopy Diagnosis")
st.write("Upload a colonoscopy image to get the predicted diagnosis.")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption='Uploaded Image', use_column_width=True)
    st.write("Analyzing...")

    prediction = predict_image(image)
    st.success(f"Prediction: *{prediction}*")
