# 🍎 CNN Fruit Freshness Classifier

A deep learning web application that classifies fruits as **Fresh** or **Rotten** using a Convolutional Neural Network (CNN) built with TensorFlow/Keras and deployed with Streamlit.

## 🚀 Features

- Upload an image of a fruit
- Automatic image resizing (224 × 224)
- Predicts whether the fruit is Fresh or Rotten
- Displays prediction confidence
- Shows the uploaded image
- Simple and user-friendly interface

## 🛠️ Tech Stack

- Python
- TensorFlow / Keras
- Streamlit
- NumPy
- Pillow

## 📂 Dataset

Dataset: **Fruits Fresh and Rotten for Classification**

Classes:
- Fresh Apples
- Fresh Bananas
- Fresh Oranges
- Rotten Apples
- Rotten Bananas
- Rotten Oranges

The model converts these into binary labels:

- **0 → Fresh**
- **1 → Rotten**

## 🧠 Model Architecture

- Data Augmentation
- Conv2D (32 Filters)
- Batch Normalization
- MaxPooling2D
- Conv2D (64 Filters)
- Batch Normalization
- MaxPooling2D
- Conv2D (128 Filters)
- Batch Normalization
- MaxPooling2D
- GlobalAveragePooling2D
- Dense (256, ReLU)
- Batch Normalization
- Dropout (0.5)
- Dense (1, Sigmoid)

## 📊 Model Performance

| Metric | Score |
|--------|-------|
| Training Accuracy | **97%** |
| Validation Accuracy | **96%+** |
| Test Accuracy | **96.92%** |

## 📁 Project Structure

```
CNN-Fruit-Freshness-Classifier/
│
├── app.py
├── fruit_classifier.keras
├── requirements.txt
├── README.md
```

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/dilip9045/CNN-Fruit-Freshness-Classifier.git
```

Move into the project directory

```bash
cd CNN-Fruit-Freshness-Classifier
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```

## 📷 Application Workflow

1. Upload a fruit image.
2. Image is resized to **224 × 224**.
3. The trained CNN model processes the image.
4. Prediction is generated.
5. Confidence score is displayed.
6. Uploaded image is shown alongside the prediction.

## 📌 Future Improvements

- Support multiple fruit categories
- Mobile-friendly interface
- Real-time camera prediction
- Grad-CAM visualization
- Transfer Learning (EfficientNet / MobileNet)

## 👨‍💻 Author

**Dilip Thakur**

GitHub: https://github.com/dilip9045

---

⭐ If you found this project useful, consider giving it a star on GitHub.
