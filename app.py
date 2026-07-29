# Import libraries for the Streamlit web application, data handling,
# and model loading
import streamlit as st
import numpy as np
import tensorflow as tf
from PIL import Image

# Configure the Streamlit web application's title, icon, and page layout
st.set_page_config(page_title="Tomato Disease Classifier", page_icon="🍅", layout="centered")

# Class order matches class_names from image_dataset_from_directory (alphabetical)
CLASS_NAMES = ["Bacterial_spot", "Target_Spot"]
IMAGE_HEIGHT, IMAGE_WIDTH = 128, 128

# Load the model from the models/ folder
@st.cache_resource
def load_model():
    model = tf.keras.models.load_model("model.keras")
    return model

# Write the predict function
def predict(model, pil_image):
    """Make prediction and return probabilities"""
    img = pil_image.convert("RGB").resize((IMAGE_WIDTH, IMAGE_HEIGHT))
    arr = np.expand_dims(np.array(img, dtype=np.float32), axis=0)
    prob_target_spot = float(model.predict(arr, verbose=0)[0][0])
    prob_bacterial_spot = 1.0 - prob_target_spot
    label = CLASS_NAMES[1] if prob_target_spot >= 0.5 else CLASS_NAMES[0]
    return label, prob_bacterial_spot * 100, prob_target_spot * 100

# Build the User Interface (UI)
st.title("🍅 Tomato Leaf Disease Classifier")
st.write("Upload a tomato leaf image to detect **Target Spot** or **Bacterial Spot**.")

model = load_model()
uploaded_file = st.file_uploader("Upload a tomato leaf image", type=["jpg", "jpeg", "png"])

# Make predictions and display the results
if uploaded_file:
    img = Image.open(uploaded_file)
    st.image(img, width=300)
    label, bacterial_pct, target_pct = predict(model, img)
    st.write(f"**Prediction:** {label.replace('_', ' ')}")
    st.progress(int(target_pct), text=f"Target Spot: {target_pct:.1f}%")
    st.progress(int(bacterial_pct), text=f"Bacterial Spot: {bacterial_pct:.1f}%")
