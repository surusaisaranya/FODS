import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import accuracy_score,mean_squared_error

from sklearn.preprocessing import StandardScaler,LabelEncoder
data = {
"bedrooms":[2,3,1,4,2,3,1,4],
"area":[2000,3000,1000,4000,2000,3000,1000,4000],
"price":[10000,20000,5000,30000,10000,20000,5000,2000],
"location":['A','B','C','D','A','B','C','A']
    }
df = pd.DataFrame(data)
print(df)

le_location = LabelEncoder()
df['location'] = le_location.fit_transform(df['location'])
X = df[['bedrooms','area','location']]
y = df['price']

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = 0.2,random_state = 42)
model = LinearRegression()
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.fit_transform(X_test)
model.fit(X_train_scaled,y_train)
y_predict = model.predict(X_test_scaled)
mse = mean_squared_error(y_test,y_predict)
print(mse)
plt.scatter(y_test,y_predict)
plt.plot([min(y_test),max(y_test)],[min(y_test),max(y_test)])
plt.show()
