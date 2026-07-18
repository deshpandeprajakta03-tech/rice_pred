# Rice Classification using Deep Learning

## Project Overview

This project is a web-based deep learning application that identifies the variety of rice from an uploaded image. A Convolutional Neural Network (CNN) model is trained using images of five different rice varieties. The trained model is integrated with a Flask web application, allowing users to upload an image and receive the predicted rice type along with the confidence score and probability for each class.

The application can also be tested through Postman using its REST API.

---

## Rice Varieties

The model classifies the following five rice varieties:

- Arborio
- Basmati
- Ipsala
- Jasmine
- Karacadag

---

## Features

- Upload a rice image through a web interface.
- Predict the rice variety using a CNN model.
- Display the confidence score.
- Show probabilities for all five classes.
- REST API support for Postman testing.
- Simple and user-friendly interface.

---

## Technologies Used

### Programming Language

- Python

### Deep Learning

- TensorFlow
- Keras

### Web Framework

- Flask

### Libraries

- NumPy
- Pillow

### Frontend

- HTML
- CSS

---

## Dataset

The project uses the Rice Image Dataset containing images of five rice varieties.

Original dataset size:

- 75,000 images

Dataset used for training:

- 12,000 images
- 2,400 images for each rice variety

Image size:

- 128 × 128 pixels

---

## Model Architecture

A custom Convolutional Neural Network (CNN) was developed for this project.

The model consists of:

- Convolution Layers
- Batch Normalization
- Max Pooling Layers
- Global Average Pooling Layer
- Dense Layer
- Dropout Layer
- Softmax Output Layer

The model predicts one of five rice classes.

---

## Project Structure

```
rice_pred/

├── app.py
├── keras1.keras
├── requirements.txt
├── README.md
├── .gitignore

├── templates/
│      └── index.html

├── static/
│      └── style.css

└── uploads/


## API Testing

The prediction API can also be tested using Postman.

## Sample Output

Prediction:
Rice Type : Basmati
Confidence:
100%


Probability:

Arborio    : 0.0%
Basmati    : 100.0%
Ipsala     : 0.0%
Jasmine    : 0.0%
Karacadag  : 0.0%






