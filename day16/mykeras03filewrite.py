from keras.datasets import mnist
from keras import models
from keras import layers
from keras.utils import to_categorical
import cv2


img = cv2.imread('2-2.png',cv2.IMREAD_GRAYSCALE)
img2 = cv2.resize(img, (28,28))
img3 = 1-(img2.reshape((1,28*28))/255)
cv2.waitKey(0)
cv2.destroyAllWindows()



(train_images, train_labels), (test_images, test_labels) = mnist.load_data()
    
train_images = train_images.reshape((60000, 28 * 28))
train_images = train_images.astype('float32') / 255
test_images = test_images.reshape((10000, 28 * 28))
test_images = test_images.astype('float32') / 255

train_labels = to_categorical(train_labels)
test_labels = to_categorical(test_labels)


model = models.Sequential()
model.add(layers.Dense(512, activation='relu', input_shape=(28 * 28,)))
model.add(layers.Dense(10, activation='softmax'))

model.compile(optimizer='rmsprop',
                loss='categorical_crossentropy',
                metrics=['accuracy'])
 
 
model.fit(train_images, train_labels, epochs=5, batch_size=128)

print("-------------------------------------------------")
print(img3)
print("-------------------------------------------------")
print(model.predict(img3))
print("-------------------------------------------------")

 
 
# test_loss, test_acc = model.evaluate(test_images, test_labels)
# print('test_acc: ', test_acc)