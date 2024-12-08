import tensorflow as tf
from PIL import Image
import numpy as np

# Load your trained model
model = tf.keras.models.load_model("keras_model.h5")

# Preprocessing function
def preprocess_image(image_path):
    image = Image.open(image_path).convert("RGB")
    image = image.resize((224, 224))  # Ensure it matches your model's input size
    image_array = np.array(image) / 255.0  # Normalize
    image_array = np.expand_dims(image_array, axis=0)  # Add batch dimension
    return image_array

# Prediction function
def predict_image(image_path):
    image_array = preprocess_image(image_path)
    prediction = model.predict(image_array)
    return prediction

if __name__ == '__main__':
    img = preprocess_image("505.jpg")
    print(predict_image(img))