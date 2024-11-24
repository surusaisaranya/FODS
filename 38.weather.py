import numpy as np
import pandas as pd

data = {
'A':[30,40,50,46,35,46],
'B':[45,34,46,56,34,43],
'C':[40,39,29,30,40,50],
'D':[30,40,33,44,33,50]
    }

df = pd.DataFrame(data)
print(df)
mean = df.mean()
print(mean)
standard_deviation = df.std()
print(standard_deviation)
range = df.max()- df.min()
print(range)
df.loc['range']=range
print(df)
print(df.loc['range'].idxmax())
df.loc['std'] = standard_deviation
print(df.loc['std'].idxmin())
