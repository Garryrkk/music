import cv2
import tensorflow as tf
import numpy as np

# Load pre-trained emotion detection model
MODEL_PATH = "recommendations/ml_models/emotion_model.h5"
model = tf.keras.models.load_model(MODEL_PATH)

# Mapping of emotion labels
EMOTION_LABELS = ["Happy", "Sad", "Neutral", "Angry", "Surprised"]

def detect_emotion(image_path):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    resized = cv2.resize(gray, (48, 48))
    reshaped = resized.reshape(1, 48, 48, 1) / 255.0
    prediction = model.predict(reshaped)
    emotion = EMOTION_LABELS[np.argmax(prediction)]
    return emotion
