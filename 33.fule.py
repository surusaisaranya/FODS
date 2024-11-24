import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error,r2_score
from sklearn.preprocessing import StandardScaler

data = {
'fuel':[10,20,30,40,50,60,70,80,90],
'price':[10000,20000,30000,40000,50000,60000,70000,80000,90000],
'engine':[1.5,2.0,3.0,3.5,4.0,4.5,5.0,5.5,6.0]
    }

df = pd.DataFrame(data)
print(df)
X  = df[['fuel','engine']]
y = df['price']
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size =0.2,random_state = 42)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.fit_transform(X_test)
model = LinearRegression()
model.fit(X_train_scaled,y_train)
y_predict = model.predict(X_test_scaled)

mse = mean_squared_error(y_test,y_predict)
print(mse)
r2score = r2_score(y_test,y_predict)
print(r2score)

plt.scatter(y_test,y_predict)
plt.plot([min(y_test),max(y_test)],[min(y_test),max(y_test)])
plt.show()


