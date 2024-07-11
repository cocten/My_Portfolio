import pandas as pd
#import numpy as np
import matplotlib.pyplot as plt
# import seaborn as sns
import sklearn
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import VotingRegressor
from sklearn.metrics import mean_squared_error

X, y = load_diabetes(return_X_y=True)
df1 = pd.DataFrame(X, columns=["age","sex","bmi","bp", "tc", "ldl", "hdl","tch", "ltg", "glu"])
df2 = pd.DataFrame(y, columns=["disease_progression"])
df = pd.merge(df1,df2, left_index=True, right_index=True)
y = df.disease_progression
X = df.drop(['disease_progression'], axis=1)

X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=1) #切割設置 X_T, n =309 . X_V, n = 133
X_train.shape, X_val.shape, y_train.shape,y_val.shape

#RandomForestRegressor
model_RF = RandomForestRegressor(n_estimators=3000, max_depth=15, random_state=1).fit(X_train, y_train)
print("RF訓練準確率",model_RF.score(X_train, y_train))
print("RF預測準確率",model_RF.score(X_val, y_val))
# 拿訓練好的模型，透過該段程式碼進行預測
pred_RF = model_RF.predict(X_val)
rms = mean_squared_error(y_val, pred_RF, squared=True)
print("RF的rms值:",rms )
print("--------------------------------")

#LinearRegression
model_LR = LinearRegression().fit(X_train, y_train)
pred_LR = model_LR.predict(X_val)
print("LR訓練準確率",model_LR.score(X_train, y_train))
print("LR預測準確率",model_LR.score(X_val, y_val))
# 拿訓練好的模型，透過該段程式碼進行預測
pred_LR = model_LR.predict(X_val)
rms = mean_squared_error(y_val, pred_LR, squared=True)
print("LR的rms值:",rms )



plt.figure(figsize=(10,10))
plt.scatter(y_val, pred_RF, c='crimson')
plt.yscale('log')
plt.xscale('log')

p1 = max(max(pred_RF), max(y_val))
p2 = min(min(pred_RF), min(y_val))
plt.plot([p1, p2], [p1, p2], 'b-')
plt.xlabel('Actual Values', fontsize=15)
plt.ylabel('Predictions', fontsize=15)
plt.axis('equal')
plt.show()

plt.figure(figsize=(10,10))
plt.scatter(y_val, pred_LR, c='crimson')
plt.yscale('log')
plt.xscale('log')

p1 = max(max(pred_LR), max(y_val))
p2 = min(min(pred_LR), min(y_val))
plt.plot([p1, p2], [p1, p2], 'b-')
plt.xlabel('Actual Values', fontsize=15)
plt.ylabel('Predictions', fontsize=15)
plt.axis('equal')
plt.show()

