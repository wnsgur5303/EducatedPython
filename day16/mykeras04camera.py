import tensorflow as tf
from tensorflow import keras
 
import numpy as np
import matplotlib.pyplot as plt
import cv2

img = cv2.imread('2-2.png',cv2.IMREAD_GRAYSCALE)
img2 = cv2.resize(img, (28,28))

img3 = 1- (img2.reshape((1,28*28))/255)

# print(img3)
#  
# for i in img2:
#     for j in i:
#         if j > 10:
#             print(" ",end=" ")
#         else:
#             print("0", end=" ")   
#     print()
# cv2.imshow('Test Image',img)

cv2.waitKey(0)
cv2.destroyAllWindows()
