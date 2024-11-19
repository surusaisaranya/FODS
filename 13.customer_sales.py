import pandas as pd
import numpy as np

data = {

'customer_id':[1,2,3,4,1],
'name':['A','B','C','D','A'],
'age':[12,10,20,30,35],
'amount':[100,200,200,300,400]
    }

df = pd.DataFrame(data)
print("Data can be as follows \n",df)

frequency = df.groupby('customer_id')['age'].count()
print(frequency)

