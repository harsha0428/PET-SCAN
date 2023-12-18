from PIL import Image
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import os

save_directory = 'models/best-model'
os.makedirs(save_directory, exist_ok=True)  # Create the directory if it doesn't exist

MODEL_PATH = 'models/best-model.h5'  # Without the file extension

# Assuming you already have a 'best-model' in the 'models' folder
model = load_model(MODEL_PATH)

def predict_image(image_path):
    img = Image.open(image_path)
    img = img.resize((224, 224))  # Resize the image as needed
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0

    prediction = model.predict(img_array)
    # Add post-processing logic based on your model output format
    # Here, we assume it returns an array with probabilities for each class.

    labels = ['Earmites', 'flea allergy', 'healthy', 'leprosy', 'pyoderma', 'ringworm']
    predicted_label = labels[np.argmax(prediction)]

    return predicted_label


 
