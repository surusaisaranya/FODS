import numpy as np
import pandas as pd

data = {
'prices':[10000,11000,12000,13000,1200,100],
'quantities':[1,2,1,2,3,4],
'discount':[20,10,30,90,22,66],
'taxrate':[11,12,10,13,9,10],
'customer':['A','A','B','C','C','B']
    }

df = pd.DataFrame(data)
print(df)

cost = df['prices']*df['quantities']*(1-df['discount']/100)*(1+df['taxrate']/100)
print(cost)

df['cost']= (cost)
print(df)

group_customers = df.groupby('customer')['cost'].sum()
print(group_customers)
