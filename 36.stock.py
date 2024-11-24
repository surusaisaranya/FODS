import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = {

'date':['2023-01-01','2023-01-02','2024-01-03','2024-01-04','2024-01-05'],
'stock':[50,60,20,70,80]
    }

df = pd.DataFrame(data)
print(df)

mean = df['stock'].mean()
std = df['stock'].std()
range = df['stock'].max()-df['stock'].min()
print(range)
print(mean)
print(std)

plt.scatter(df['date'],df['stock'])
plt.plot(df['stock'] , c = 'red')
plt.show()
