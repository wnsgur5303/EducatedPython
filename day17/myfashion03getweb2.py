import tensorflow as tf
import cv2
import keras
from tensorflow.python.keras.models import load_model
from keras.layers import Flatten
import numpy as np



img = cv2.imread('baj.jpg',cv2.IMREAD_GRAYSCALE)
img2 = cv2.resize(img, (28,28))
img3 = 1- (img2.reshape((1,28*28))/255)
cv2.waitKey(0)
cv2.destroyAllWindows()

model = load_model("mymodel")

img_np = model.predict(img3)
index = np.argmax(img_np[0])

print("-------------------------------------------------")
print(img3)
print("-------------------------------------------------")
print(index)
print("-------------------------------------------------")
