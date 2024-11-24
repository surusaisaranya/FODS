import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
data = {

'cust_id':[1,2,3,4,5],
'amount':[100,200,300,300,250],
'number':[2,3,1,2,3]
    }

df = pd.DataFrame(data)
print(df)

X = df[['cust_id','number']]
y = df['amount']
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = 0.2,random_state = 42)
model = KNeighborsClassifier(n_neighbors=min(len(X_train), 5))
model.fit(X_train,y_train)
y_predict = model.predict(X_test)
cm = confusion_matrix(y_test,y_predict)
print(cm)
plt.scatter(X_train['cust_id'],X_train['number'] , c= y_train )
plt.scatter(X_test['cust_id'],X_test['number'] , c = y_test )
plt.show()
