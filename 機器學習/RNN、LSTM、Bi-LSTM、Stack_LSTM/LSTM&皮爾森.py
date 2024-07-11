#-------------資料前處理-----------
# from pandas import read_csv
# from datetime import datetime
# dataset = read_csv('91-Site_1A-Trina(2014-2021).csv',index_col="timestamp")
# dataset.drop(labels=["Active_Energy_Delivered_Received","Current_Phase_Average"], axis="columns",inplace=True)
# # manually specify column names(從先新編輯檔案列的名稱)
# dataset.columns = ['A.P', 'W.S', 'W.T.C', 'W.R.H', 'G.H.R', 'D.H.R', 'W.D','W.D.R','R.G.T','R.D.T']
# dataset.index.name = 'time'#更改檔案的標題
# # mark all NA values with 0
# dataset.fillna(0, inplace=True)#fillna(把NaN值換成0,直接寫入資料內)
# # save to file
# dataset.to_csv('1A_solar_energy_pollution.csv')

# from matplotlib import pyplot
# import seaborn as sns
# # load dataset
# dataset = read_csv('1A_solar_energy_pollution', header=0, index_col=0)#呼叫檔案，從第一列開始header=0,從第一行開始 index_col=0

# pyplot.figure(figsize=(9,7))
# sns.heatmap(dataset.corr(),annot = True,cmap ='YlOrRd',square =True)
# pyplot.title('1A_solar_energy_pollution.csv',fontsize = 18,pad ='20')
# pyplot.show()

# dataset.describe().loc[['mean', 'std','min','max']]

# values = dataset.values#將資料轉為數值
# # specify columns to plot
# groups = [0,1, 2, 3, 5, 6, 7,8,9]
# i = 1
# # plot each column
# pyplot.figure()#畫圖指令
# for group in groups:
#     pyplot.subplot(len(groups), 1, i)#subplot(行,列,第幾筆資料)
#     pyplot.plot(values[:, group])#(values[:選取全部資料,從第幾筆資料])
#     pyplot.title(dataset.columns[group], y=0.5, loc='right')#寫標題title(選取第幾筆標題,Y軸位置,標題要在哪邊顯示)
#     i += 1
# pyplot.show()


#---------開始訓練-------------
# prepare data for lstm  為lstm準備數據
from math import sqrt
from numpy import concatenate,mean
from matplotlib import pyplot
from pandas import read_csv,DataFrame,concat 
from sklearn.preprocessing import MinMaxScaler,LabelEncoder
from sklearn.metrics import mean_squared_error,mean_absolute_error,mean_absolute_percentage_error,r2_score
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense,Dropout,LSTM,GRU,SimpleRNN,RNN,Bidirectional
import datetime
import time
import seaborn as sns

#----皮爾森分析熱力圖--------
originaldataset = read_csv('./1A-test(2013-2016).csv', header=0, index_col=0)
pyplot.figure(figsize=(9,7))
sns.heatmap(originaldataset.corr(),annot = True,cmap ='YlOrRd',square =True)
pyplot.title('1A_solar_energy_pollution',fontsize = 18,pad ='20')
pyplot.show()
#pyplot.savefig("1A_solar_energy_Pearson.jpg")

start = time.time()
startT = datetime.datetime.now()
print("開始時間",startT)

# convert series to supervised learning將序列轉換為監督學習
def series_to_supervised(data, n_in=1, n_out=1, dropnan=True):
    n_vars = 1 if type(data) is list else data.shape[1]
    df = DataFrame(data)
    cols, names = list(), list()
    # input sequence (t-n, ... t-1)輸入序列 (t-n, ... t-1)
    for i in range(n_in, 0, -1):
        cols.append(df.shift(i))
        names += [('var%d(t-%d)' % (j+1, i)) for j in range(n_vars)]
    # forecast sequence (t, t+1, ... t+n)預測序列 (t, t+1, ... t+n)
    for i in range(0, n_out):
        cols.append(df.shift(-i))
        if i == 0:
            names += [('var%d(t)' % (j+1)) for j in range(n_vars)]
        else:
            names += [('var%d(t+%d)' % (j+1, i)) for j in range(n_vars)]
    # put it all together 把他們放在一起
    agg = concat(cols, axis=1)
    agg.columns = names 
    # drop rows with NaN values刪除具有 NaN 值的行
    if dropnan:
        agg.dropna(inplace=True)
    return agg

# load dataset 載入資料
dataset = read_csv('1A_solar_energy_Pearson.csv', header=0, index_col=0)#呼叫檔案，從第一列開始header=0,從第一行開始 index_col=0
values = dataset.values
# ensure all data is float 確保所有數據都是浮動的
values = values.astype('float32')#將數據轉為浮點數去除小數點後的數字
# normalize features 正規劃特徵
scaler = MinMaxScaler(feature_range=(0, 1))#將特徵縮放在0跟1之間
scaled = scaler.fit_transform(values)
# frame as supervised learning 框架作為監督學習
reframed = series_to_supervised(scaled, 1, 1)#將數據匯入涵式
reframed.drop(reframed.columns[[5,6,7]], axis=1, inplace=True) #刪除不要使用的數據，保留預測數據
# split into train and test sets 分成訓練集和測試集
values = reframed.values
n_train_hours =  int(values.shape[0]*0.7)
train = values[:n_train_hours, :]
test = values[n_train_hours:, :]

Neurons = [32,64,128,256,512]
epochs =[50,100,150,200]
batch_size =[500,1000,2000,3000,4000,5000] 

for n in Neurons:
    for e in epochs:
        for b in batch_size:
            all_rmse = []
            all_mse = []
            all_mae = []
            all_r2 = []
            for i in range(1,31,1):
                print('第',i,'次測試')
                print('神經元'+str(n)+'批次大小'+str(b)+'迭代'+str(e))
                # split into input and outputs 分為輸入和輸出
                train_X, train_y = train[:, :-1], train[:, -1]
                test_X, test_y = test[:, :-1], test[:, -1]
                # reshape input to be 3D [samples, timesteps, features] 將輸入重塑為 3D [樣本、時間步長、特徵]
                train_X = train_X.reshape((train_X.shape[0], 1, train_X.shape[1]))
                test_X = test_X.reshape((test_X.shape[0], 1, test_X.shape[1]))
                #print(train_X.shape, train_y.shape, test_X.shape, test_y.shape)
                # from sklearn.model_selection import GridSearchCV
                from tensorflow import keras
                # design network 架設模型
                model = Sequential()
                model.add(LSTM(n, input_shape=(train_X.shape[1], train_X.shape[2]),return_sequences = False))#,return_sequences = False,activation = 'relu'
                #model.add(Dropout(0.2))#適狀況使用
                model.add(Dense(32))
                model.add(Dense(1))#,activation='relu'
                #adam = keras.optimizers.Adam(learning_rate=0.01) #調整學習率(適狀況使用)
                model.compile(loss='mae', optimizer='adam')#,metrics=['mae']
                #model.summary()#檢視模型架構
                # fit network 訓練模型找適配度
                history = model.fit(train_X, train_y, epochs=e ,batch_size=b, validation_data=(test_X, test_y), verbose=2, shuffle=False )
                #make a prediction 進行預測
                yhat = model.predict(test_X,verbose=2)
                test_X = test_X.reshape((test_X.shape[0], test_X.shape[2]))
                # invert scaling for forecast 用於預測的反轉縮放 
                inv_yhat = concatenate((yhat, test_X[:, 1:]), axis=1)
                inv_yhat = scaler.inverse_transform(inv_yhat)
                inv_yhat = inv_yhat[:,0]
                # invert scaling for actual 實際反轉縮放   
                test_y = test_y.reshape((len(test_y), 1))
                inv_y = concatenate((test_y, test_X[:, 1:]), axis=1)
                inv_y = scaler.inverse_transform(inv_y)
                inv_y = inv_y[:,0]
                # calculate RMSE 計算RMSE
                rmse = sqrt(mean_squared_error(inv_y, inv_yhat))
                mse = mean_squared_error(inv_y, inv_yhat)
                mae = mean_absolute_error (inv_y, inv_yhat)
                r2 =r2_score(inv_y, inv_yhat)
                all_rmse.append(rmse)
                all_mse.append(mse)
                all_mae.append(mae)
                all_r2.append(r2)
                #all_mape.append(mape)
                print('Test RMSE: %.3f' % rmse)
                print('Test MSE: %.3f' % mse)
                print('Test MAE: %.3f' % mae)
                print('Test R2: %.3f' % r2)
                del model
            all_rmse.append(round(mean(all_rmse),3))
            all_mse.append(round(mean(all_mse),3))
            all_mae.append(round(mean(all_mae),3))
            all_r2.append(round(mean(all_r2),3))
            from pandas import DataFrame
            #RMSE
            all_rmse_mean =  DataFrame(all_rmse,columns = ['RMSE'])
            #all_rmse_mean.to_csv("/home/ncutroom/下載/YUJIA/模型設定_Dense(32)_Dense(1)/BiLSTM(GPU)/1A_(NP)BiLSTM_神經元"+str(n)+"_迭代"+str(e)+"_批次大小"+str(b)+"_rmse_mean_Dense(32)_Dense(1).csv", index=False)
            #MSE
            all_mse_mean =  DataFrame(all_mse,columns = ['MSE'])
            #all_mse_mean.to_csv("/home/ncutroom/下載/YUJIA/模型設定_Dense(32)_Dense(1)/BiLSTM(GPU)/1A_(NP)BiLSTM_神經元"+str(n)+"_迭代"+str(e)+"_批次大小"+str(b)+"_mse_mean_Dense(32)_Dense(1).csv", index=False)
            #MAE
            all_mae_mean =  DataFrame(all_mae,columns = ['MAE'])
            #all_mae_mean.to_csv("/home/ncutroom/下載/YUJIA/模型設定_Dense(32)_Dense(1)/BiLSTM(GPU)/1A_(NP)BiLSTM_神經元"+str(n)+"_迭代"+str(e)+"_批次大小"+str(b)+"_mae_mea_Dense(32)_Dense(1).csv", index=False)
            #R^2
            all_r2_mean =  DataFrame(all_r2,columns = ['R^2'])
            #all_r2_mean.to_csv("/home/ncutroom/下載/YUJIA/模型設定_Dense(32)_Dense(1)/BiLSTM(GPU)/1A_(NP)BiLSTM_神經元"+str(n)+"_迭代"+str(e)+"_批次大小"+str(b)+"_r2_mean_Dense(32)_Dense(1).csv", index=False)
            #print(all_rmse[:-1])
            print('all_rmse_mean: ',(all_rmse[-1:]))
            #print(all_mse[:-1])
            print('all_mse_mean: ',(all_mse[-1:]))
            #print(all_mae[:-1])
            print('all_mae_mean: ',(all_mae[-1:]))
            #print(all_r2[:-1])
            print('all_r^2_mean: ',(all_r2[-1:]))
            del all_rmse_mean            
            del all_mse_mean            
            del all_mae_mean          
            del all_r2_mean
            import gc
            gc.collect()


print("開始時間",startT)
Atime = datetime.datetime.now()
print("演算時間",Atime)
end = time.time()
print("運行時間：%s秒"%(round((end-start),5)))


from numba import cuda
cuda.select_device(0)
cuda.close()

import gc
gc.collect()


