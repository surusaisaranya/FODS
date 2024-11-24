import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score,precision_score,f1_score,recall_score
from sklearn.preprocessing import StandardScaler,LabelEncoder
data = {

"age":[40,50,60,70,50],
"gender":['F','M','F','M','M'],
"bp":[110,120,100,120,90],
"cho_level":[30,10,20,30,40],
"respond":["Good","Bad","Good","Good","Good"]

    }

df = pd.DataFrame(data)
print(df)
le_gender = LabelEncoder()
le_respond = LabelEncoder()
df['gender'] = le_gender.fit_transform(df['gender'])
df['respond']= le_respond.fit_transform(df['respond'])

X = df[['age','gender','bp','cho_level']]
y = df['respond']
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = 0.2,random_state = 42)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.fit_transform(X_test)
model = KNeighborsClassifier(n_neighbors = min(len(X_train),5))
model.fit(X_train_scaled,y_train)
y_predict = model.predict(X_test_scaled)
accuracy = accuracy_score(y_test,y_predict)
print(accuracy)
recall = recall_score(y_test,y_predict,zero_division = 1)
print(recall)
precision = precision_score(y_test,y_predict , zero_division = 1)
print(precision)

