from flask import Flask, render_template, request, jsonify
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import os

app = Flask(__name__)

# Upload folder
UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Create uploads folder if it doesn't exist
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Load trained model
model = load_model("keras1.keras")

# Class names (same order used during training)
class_names = [
    "Arborio",
    "Basmati",
    "Ipsala",
    "Jasmine",
    "Karacadag"
]


# Home Page
@app.route("/")
def home():
    return render_template("index.html")


# Prediction API
@app.route("/predict", methods=["POST"])
def predict():

    # Check if file exists
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"})

    file = request.files["file"]

    # Check if filename is empty
    if file.filename == "":
        return jsonify({"error": "No file selected"})

    # Save uploaded image
    filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
    file.save(filepath)

    # Load image
    img = image.load_img(filepath, target_size=(128, 128))

    # Convert image to array
    img_array = image.img_to_array(img)

    # Normalize
    img_array = img_array / 255.0

    # Add batch dimension
    img_array = np.expand_dims(img_array, axis=0)

    # Predict
    prediction = model.predict(img_array)[0]

    # Predicted class index
    predicted_index = np.argmax(prediction)

    # Predicted class name
    predicted_class = class_names[predicted_index]

    # Confidence
    confidence = float(prediction[predicted_index] * 100)

    # Probability for every class
    probabilities = {}

    for i in range(len(class_names)):
        probabilities[class_names[i]] = round(float(prediction[i] * 100), 2)

    # Response
    return jsonify({
        "prediction": predicted_class,
        "confidence": round(confidence, 2),
        "probabilities": probabilities,
        "image": file.filename
    })


# Run Flask App
if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=8000,
        debug=True
    )