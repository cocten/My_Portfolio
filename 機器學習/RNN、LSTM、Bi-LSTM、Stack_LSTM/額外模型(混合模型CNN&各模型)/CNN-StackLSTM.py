# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 21:52:42 2024

@author: Yu-Chia
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow import keras
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error,mean_absolute_error,mean_absolute_percentage_error,r2_score
import gc
import datetime
import time

start = time.time()
startT = datetime.datetime.now()
print("開始時間",startT)

all_rmse = []
all_mse = []
all_mae = []
all_r2 = []

def split_windows(data, size):
    X = []
    Y = []
    for i in range(len(data) - size):
        X.append(data[i:i+size, :])
        Y.append(data[i+size, 2])
    return np.array(X), np.array(Y)

data = pd.read_csv('./1A_solar_energy(2013-2016).csv', header=0, index_col=0)
all_data = data.values
train_len = int(all_data.shape[0]*0.7)
train_data = all_data[:train_len, :]
test_data = all_data[train_len:, :]

plt.figure(figsize=(12, 8))
plt.plot(np.arange(train_data.shape[0]), train_data[:, 0], label='AP train data')
plt.plot(np.arange(train_data.shape[0], train_data.shape[0] + test_data.shape[0]), test_data[:, 0], label='AP test data')
plt.legend()
plt.show()

# normalizatioin processing(正規化資料集)
scaler = MinMaxScaler(feature_range=(0, 1))
scaled_train_data = scaler.fit_transform(train_data)
scaled_test_data = scaler.transform(test_data)
for i in range(1,31,1):
    print('第',i,'次測試')
    # 轉換資料型態，並拆分訓練集與測試集
    window_size = 10
    train_X, train_Y = split_windows(scaled_train_data, size=window_size)
    test_X, test_Y = split_windows(scaled_test_data, size=window_size)
    fea_num = 10
    model = keras.models.Sequential([
        keras.layers.Input((window_size, fea_num)),
        keras.layers.Reshape((window_size, fea_num, 1)),
        keras.layers.Conv2D(filters=64,
                               kernel_size=3,
                               strides=1,
                               padding="same",
                               activation="relu"),
        keras.layers.MaxPooling2D(pool_size=2, strides=1, padding="same"),
        keras.layers.Dropout(0.3),
        keras.layers.Reshape((window_size, -1)),#將資料轉為三維帶入時間序列模型
        keras.layers.LSTM(128, return_sequences=True),
        keras.layers.LSTM(32, return_sequences=False),
        #keras.layers.Dense(32, activation="relu"),
        keras.layers.Dense(1)
    ])
    model.compile(loss='mae', optimizer='adam', metrics=['mae'])
    # model.summary()
    history = model.fit(train_X,train_Y, epochs = 200 ,batch_size = 5000,validation_data=(test_X, test_Y),verbose=0)
    plt.plot(history.history['loss'], label='train')
    plt.plot(history.history['val_loss'], label='test')
    plt.legend()
    #plt.savefig("CNNLSTM(視窗100卷積64)")
    plt.show()
    prediction = model.predict(test_X,verbose = 0)
    scaled_prediction = prediction * (scaler.data_max_[0] - scaler.data_min_[0]) + scaler.data_min_[0]
    scaled_true = test_Y * (scaler.data_max_[0] - scaler.data_min_[0]) + scaler.data_min_[0]
    # plt.plot(range(len(scaled_prediction)), scaled_prediction, label='true')
    # plt.plot(range(len(scaled_true)), scaled_true, label='prediction')#, marker='*'
    # plt.legend()
    rmse = np.sqrt(mean_squared_error(scaled_prediction, scaled_true))
    mse = mean_squared_error(scaled_prediction, scaled_true)
    mae = mean_absolute_error (scaled_prediction, scaled_true)
    r2 =r2_score(scaled_prediction, scaled_true)
    all_rmse.append(rmse)
    all_mse.append(mse)
    all_mae.append(mae)
    all_r2.append(r2)
    print('Test RMSE: %.3f' % rmse)
    print('Test MSE: %.3f' % mse)
    print('Test MAE: %.3f' % mae)
    print('Test R2: %.3f' % r2)
    del model
    del rmse
    del mse
    del mae
    del r2
   

all_rmse.append(round(np.mean(all_rmse),3))
all_mse.append(round(np.mean(all_mse),3))
all_mae.append(round(np.mean(all_mae),3))
all_r2.append(round(np.mean(all_r2),3))

# from pandas import DataFrame
# #RMSE
# all_rmse_mean =  DataFrame(all_rmse,columns = ['RMSE'])
# all_rmse_mean.to_csv("1A_CNNLSTM(視窗100卷積64)_rmse_mean.csv", index=False)
# #MSE
# all_mse_mean =  DataFrame(all_mse,columns = ['MSE'])
# all_mse_mean.to_csv("1A_CNNLSTM(視窗100卷積64)_mse_mean.csv", index=False)
# #MAE
# all_mae_mean =  DataFrame(all_mae,columns = ['MAE'])
# all_mae_mean.to_csv("1A_CNNLSTM(視窗100卷積64)_mae_mean.csv", index=False)
# #R^2
# all_r2_mean =  DataFrame(all_r2,columns = ['R^2'])
# all_r2_mean.to_csv("1A_CNNLSTM(視窗100卷積64)_r2_mean.csv", index=False)

print('all_rmse_mean: ',(all_rmse[-1:]))
print('all_mse_mean: ',(all_mse[-1:]))
print('all_mae_mean: ',(all_mae[-1:]))
print('all_r^2_mean: ',(all_r2[-1:]))

gc.collect()

print("開始時間",startT)
Atime = datetime.datetime.now()
print("演算時間",Atime)
end = time.time()
print("運行時間：%s秒"%(round((end-start),5)))