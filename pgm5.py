
#pip install ultralytics
from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2, preprocess_input, decode_predictions
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import numpy as np

# Load pretrained model
model = MobileNetV2(weights="imagenet")

# Load and preprocess image
img_path = "image3.jpg"   # <-- replace with your image file
img = load_img(img_path, target_size=(224, 224))
x = img_to_array(img)
x = np.expand_dims(x, axis=0)
x = preprocess_input(x)

# Predict
predictions = model.predict(x)
label = decode_predictions(predictions, top=1)[0][0]

print("Predicted:", label[1], " — Confidence:", round(label[2] * 100, 2), "%")
