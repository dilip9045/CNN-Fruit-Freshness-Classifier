import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Fruit Freshness Classifier",
    page_icon="🍎",
    layout="centered"
)

# -----------------------------
# Load Model
# -----------------------------
@st.cache_resource
def load_model():
    return tf.keras.models.load_model(
    "fruit_fresh_rotten_classifier.h5",
    compile=False
)

model = load_model()

# -----------------------------
# Title
# -----------------------------
st.title("🍎 Fruit Freshness Classifier")
st.write("Upload a fruit image to predict whether it is Fresh or Rotten.")

# -----------------------------
# Upload Image
# -----------------------------
uploaded_file = st.file_uploader(
    "Choose an Image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:

    # Read image using Pillow
    image = Image.open(uploaded_file).convert("RGB")

    # Display image
    display_image = image.copy()
    display_image.thumbnail((500, 500))

    st.image(
        display_image,
        caption="Uploaded Image",
        use_container_width=False
    )

    # Resize for model
    prediction_image = image.resize((224, 224))

    # Convert to numpy
    img_array = np.array(prediction_image).astype(np.float32)

    # Normalize
    img_array = img_array / 255.0

    # Expand dimensions
    img_array = np.expand_dims(img_array, axis=0)

    # Predict
    prediction = model.predict(img_array, verbose=0)[0][0]

    if prediction >= 0.5:
        label = "🍂 Rotten"
        confidence = prediction * 100
    else:
        label = "🍏 Fresh"
        confidence = (1 - prediction) * 100

    st.markdown("---")

    st.subheader("Prediction")

    if prediction >= 0.5:
        st.error(label)
    else:
        st.success(label)

    st.write(f"### Confidence : {confidence:.2f}%")

    st.progress(float(confidence / 100))

    st.markdown("---")

    st.write("Model Output")

    st.code(f"Raw Prediction : {prediction:.4f}")

    st.info("""
Prediction < 0.50 → Fresh

Prediction ≥ 0.50 → Rotten
""")

# -----------------------------
# Sidebar
# -----------------------------
st.sidebar.title("Model Information")

st.sidebar.write("""
**Framework:** TensorFlow

**Architecture:** CNN

**Input Size:** 224 × 224

**Classes**

🍏 Fresh

🍂 Rotten

**Test Accuracy**

96.92%
""")