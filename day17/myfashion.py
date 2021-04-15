# tensorflow와 tf.keras를 임포트합니다
import tensorflow as tf
from tensorflow import keras

# 헬퍼(helper) 라이브러리를 임포트합니다
import numpy as np
import matplotlib.pyplot as plt
import cv2

print(tf.__version__) #2.3.0

## 1.패션 MNIST 데이터셋 임포트하기

#10개의 범주& 70,000개의 흑백 이미지로 구성
# => train_images 60,000개로 학습+ test_images 10,000개의 이미지로 평가

fashion_mnist = keras.datasets.fashion_mnist

#load_data(): 4개의 NumPy 배열 반환 (train_images, train_labels)&(test_images와 test_labels)
#NumPy 배열: 28x28 크기 이미지/ label: 0~9 =옷의 클래스
(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

for i in range(len(train_labels)):
    label = str(train_labels[i])
    cv2.imwrite("image/"+label+"_"+str(i)+'.jpg', train_images[i])
    
cv2.waitKey(0)
cv2.destroyAllWindows()
    
#각 이미지는 하나의 레이블에 매핑
#데이터셋에 클래스 이름 저장 (나중에 이미지를 출력할 때 사용)
class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

##2. 데이터 탐색

#모델 훈련전, 데이터셋 구조를 살펴보자 
#-> 훈련 세트에 60,000개,테스트 세트에는 10,000개의 이미지 각 이미지는 28x28 픽셀로 표현
#각 레이블: 0~ 9 정수-> 각 이미지가 어떤 레이블의 옷인지 예측

train_images.shape #(60000, 28, 28)
len(train_labels) #60000
train_labels #array([9, 0, 0, ..., 3, 0, 5], dtype=uint8)

test_images.shape #(10000, 28, 28)
len(test_labels) #10000

##3. 데이터 전처리
#신경망 모델에 주입하기 전, 픽셀 범위를 255로 나누어 0~1 사이로 조정
# -> 훈련 세트와 테스트 세트를 동일한 방식으로 전처리해야함

#첫 번째 이미지 픽셀 값의 범위가 0~255 라는 것을 확인
plt.figure()
plt.imshow(train_images[0])
plt.colorbar()
plt.grid(False)
plt.show()

train_images = train_images / 255.0
test_images = test_images / 255.0

#훈련 세트에서 처음 25개 이미지와 그 아래 클래스 이름을 출력해 확인
plt.figure(figsize=(10,10))
for i in range(25):
    plt.subplot(5,5,i+1)
    plt.xticks([])
    plt.yticks([])
    plt.grid(False)
    plt.imshow(train_images[i], cmap=plt.cm.binary)
    plt.xlabel(class_names[train_labels[i]])
    
plt.show()

##4. 모델 구성
# 모델의 층 설정-> 컴파일

#층 설정
#층: 신경망의 기본 구성 요소 -> 주입된 데이터에서 (의미있는) 표현을 추출
#딥러닝은 간단한 층을 연결하여 구성되기 때문에 가중치는 훈련하는 동안 학습됨

#네트워크의 1번째 층-> 학습되는 가중치가 없고 데이터를 변환하기만 
#Flatten: 2차원 배열(28 x 28 픽셀)의 이미지 포맷-> 28 * 28 = 784 픽셀의 1차원 배열로 펼쳐서 변환

#2개의 Dense층이 연결 (= 밀집'완전 연결층)
#1Dense층: 128개 노드 & 2Dense층: 10 노드의 softmax층
#2Dense층-> 10개의 확률을 반환& 반환된 전체 확률 합은 1 = 현재 이미지가 10개 클래스 중 하나에 속할 확률을 출력
model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)),
    keras.layers.Dense(128, activation='relu'),
    keras.layers.Dense(10, activation='softmax')
])

#모델 컴파일
#Loss function: 모델의 오차 측정 -> 이 함수를 최소화해야 
#Optimizer: 모델의 업데이트 방법을 결정
#Metrics: 훈련 &테스트 단계 모니터링 by. accuracy= 올바르게 분류된 이미지의 비율
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

##5. 모델 훈련
#훈련 데이터를 모델에 주입(train_images, train_labels 배열)
#모델이 이미지- 레이블을 매핑하는 방법을 학습
#test_images에 대한 모델의 예측 생성 & 이 예측이 test_labels 배열의 레이블과 맞는지 확인

#model.fit: 모델이 훈련 데이터를 학습 -> 손실과 정확도(0.88) 출력
model.fit(train_images, train_labels, epochs=5)

##6. 정확도 평가
#테스트 세트에서 모델의 성능을 비교
test_loss, test_acc = model.evaluate(test_images,  test_labels, verbose=2)

print('\n테스트 정확도:', test_acc) #테스트 정확도: 0.8683000206947327

#테스트 < 훈련 세트의 정확도 ->이유:overfitting=모델이 훈련 데이터보다 새로운 데이터에서 성능이 낮아지는 현상

##7.예측만들기

predictions = model.predict(test_images)

# 테스트 세트의 각 이미지의 레이블을 예측 ->10개의 숫자 배열(신뢰도: 얼마나 잘 맞는지) 
predictions[0]
#가장 높은 신뢰도를 가진 레이블찾기
np.argmax(predictions[0]) #9 =이 이미지가 앵클 부츠(class_name[9])라고 가장 확신
#이 값이 맞는지 테스트 레이블을 확인
test_labels[0] #9

#10개 클래스에 대한 예측을 그래프로 표현하기
def plot_image(i, predictions_array, true_label, img):
  predictions_array, true_label, img = predictions_array[i], true_label[i], img[i]
  plt.grid(False)
  plt.xticks([])
  plt.yticks([])

  plt.imshow(img, cmap=plt.cm.binary)

  predicted_label = np.argmax(predictions_array)
  if predicted_label == true_label:
    color = 'blue'
  else:
    color = 'red'

  plt.xlabel("{} {:2.0f}% ({})".format(class_names[predicted_label],
                                100*np.max(predictions_array),
                                class_names[true_label]),
                                color=color)

def plot_value_array(i, predictions_array, true_label):
  predictions_array, true_label = predictions_array[i], true_label[i]
  plt.grid(False)
  plt.xticks([])
  plt.yticks([])
  thisplot = plt.bar(range(10), predictions_array, color="#777777")
  plt.ylim([0, 1])
  predicted_label = np.argmax(predictions_array)

  thisplot[predicted_label].set_color('red')
  thisplot[true_label].set_color('blue')

#0번째 원소의 이미지, 예측, 신뢰도 점수 배열 확인
i = 0
plt.figure(figsize=(6,3))
plt.subplot(1,2,1)
plot_image(i, predictions, test_labels, test_images)
plt.subplot(1,2,2)
plot_value_array(i, predictions,  test_labels) #Anckle Boot,98%
plt.show()

#12번째 원소의 이미지, 예측, 신뢰도 점수 배열 확인
# 올바른 예측은 파랑색으로 잘못된 예측은 빨강색으로 나타냅니다
i = 12
plt.figure(figsize=(6,3))
plt.subplot(1,2,1)
plot_image(i, predictions, test_labels, test_images)
plt.subplot(1,2,2)
plot_value_array(i, predictions,  test_labels) #Sandal, 38%
plt.show()

# 처음 X 개의 테스트 이미지, 예측 레이블, 진짜 레이블을 출력
num_rows = 5
num_cols = 3
num_images = num_rows*num_cols
plt.figure(figsize=(2*2*num_cols, 2*num_rows))
for i in range(num_images):
  plt.subplot(num_rows, 2*num_cols, 2*i+1)
  plot_image(i, predictions, test_labels, test_images)
  plt.subplot(num_rows, 2*num_cols, 2*i+2)
  plot_value_array(i, predictions, test_labels)
plt.show()

#훈련된 모델을 사용하여 한 이미지에 대한 예측 만들자
# 테스트 세트에서 이미지 하나를 선택합니다
img = test_images[0]

print(img.shape) #(28, 28)

# 이미지 하나만 사용할 때도 배치(한번에 학습하는 샘플의 묶음 단위)에 추가 (2차원배열로 만들어야)
img = (np.expand_dims(img,0))
print(img.shape)#(1, 28, 28)

#이 이미지의 예측 생성 
predictions_single = model.predict(img)
print(predictions_single) 
plot_value_array(0, predictions_single, test_labels)
_ = plt.xticks(range(10), class_names, rotation=45)
np.argmax(predictions_single[0])
#9:Angkle Boot

