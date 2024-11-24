import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
data = {
"age":[20,30,40,25,36,37,48],
"churn_history":[2,3,1,5,4,3,2],
"churn_data":[0,1,1,1,0,0,1],
"amount":[1000,2000,3000,4000,5000,6000,7000]
    }

df = pd.DataFrame(data)
print(df)
X = df[['age','churn_history','amount']]
y = df['churn_data']
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = 0.2,random_state = 42)
model = LogisticRegression()
scaler = StandardScaler()
X_train_scaler = scaler.fit_transform(X_train)
X_test_scaler = scaler.fit_transform(X_test)
model.fit(X_train_scaler,y_train)
y_predict = model.predict(X_test_scaler)
features = np.array([[40,1,3000]])
features_trans = scaler.transform(features)
predictions = model.predict(features_trans)
print(predictions)
