import tensorflow as tf
import cv2 
mnist = tf.keras.datasets.mnist

# 載入 MNIST 手寫阿拉伯數字資料
(x_train, y_train),(x_test, y_test) = mnist.load_data()
#進行特徵工程，將特徵縮放成(0, 1)之間
x_train_norm, x_test_norm = x_train / 255.0, x_test / 255.0

print("X_train shape:",x_train.shape)
print("X_test shape:",x_test.shape)
print("y_train label:",y_train.shape)
print("y_test label:",y_test.shape)
# print(x_train[0])
# x_train.ndim\
    
import matplotlib.pyplot as plt
def plot_images(images,labels,prediction,idx,num=10):
    fig = plt.gcf()
    fig.set_size_inches(12, 14)
    if num>25: num=25 
    for i in range(0, num):
        ax=plt.subplot(5,5, 1+i)
        ax.imshow(images[idx], cmap='binary')
        title= "label=" +str(labels[idx])
        if len(prediction)>0:
            title+=",predict="+str(prediction[idx]) 
            
        ax.set_title(title,fontsize=10) 
        ax.set_xticks([]);ax.set_yticks([])        
        idx+=1 
    plt.show()

plot_images(x_train,y_train,[],0,10)

import matplotlib.pyplot as plt
def plot_images(images,labels,prediction,idx,num=10):
    fig = plt.gcf()
    fig.set_size_inches(12, 14)
    if num>25: num=25 
    for i in range(0, num):
        ax=plt.subplot(5,5, 1+i)
        ax.imshow(images[idx], cmap='binary')
        title= "label=" +str(labels[idx])
        if len(prediction)>0:
            title+=",predict="+str(prediction[idx]) 
            
        ax.set_title(title,fontsize=10) 
        ax.set_xticks([]);ax.set_yticks([])        
        idx+=1 
    plt.show()

plot_images(x_test,y_test,[],3,10)

# 建立模型
from tensorflow.keras import layers
import numpy as np

input_shape=(28, 28, 1)
# 增加一維在最後面
x_train_norm = np.expand_dims(x_train_norm, -1)
x_test_norm = np.expand_dims(x_test_norm, -1)

# CNN 模型
model = tf.keras.Sequential(
    [
        tf.keras.Input(shape=input_shape),
        layers.Conv2D(32, kernel_size=(3, 3), activation="relu"),
        layers.MaxPooling2D(pool_size=(2, 2)),
        layers.Conv2D(64, kernel_size=(3, 3), activation="relu"),
        layers.MaxPooling2D(pool_size=(2, 2)),
        layers.Flatten(),
        layers.Dropout(0.3),
        layers.Dense(10, activation="softmax"),
    ]
)
# model.summary()
x_train_norm.ndim
x_train_norm.shape

# 設定優化器(optimizer)、損失函數(loss)、效能衡量指標(metrics)的類別
model.compile(optimizer='adam',loss='sparse_categorical_crossentropy',metrics=['accuracy'])
# 模型訓練
history = model.fit(x_train_norm, y_train, epochs=20, validation_split=0.2,batch_size =100 )
# 評分(Score Model)
score=model.evaluate(x_test_norm, y_test, verbose=1)
for i, x in enumerate(score):
    print(f'{model.metrics_names[i]}: {score[i]:.4f}')
    
    import matplotlib.pyplot as plt
def show_history(train_acc,test_acc):
    plt.plot(history.history[train_acc])
    plt.plot(history.history[test_acc])
    plt.title('Train History')
    plt.ylabel('Accuracy')
    plt.xlabel('Epoch')
    plt.legend(['train', 'test'], loc='upper left')
    plt.show()
show_history('accuracy','val_accuracy')

import matplotlib.pyplot as plt
def show_history(train_acc,test_acc):
    plt.plot(history.history[train_acc])
    plt.plot(history.history[test_acc])
    plt.title('Train History')
    plt.ylabel('Loss')
    plt.xlabel('Epoch')
    plt.legend(['train', 'test'], loc='upper left')
    plt.show()
show_history('loss','val_loss')

del model
