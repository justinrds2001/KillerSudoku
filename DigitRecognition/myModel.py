import cv2
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt


# Load the trained model
model = tf.keras.models.load_model('MNIST_2by2poolsize_5epochs.h5')

# Preprocess the image
img = cv2.imread('C:/Users/diren/Downloads/pixil-frame-0.png', cv2.IMREAD_GRAYSCALE)
img = cv2.resize(img, (28, 28))
img = np.expand_dims(img, axis=0)
img = img.astype('float32') / 255.0

# Make predictions
pred = model.predict(img)
digit = np.argmax(pred)

# Print the predicted digit
print(digit)