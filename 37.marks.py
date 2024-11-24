import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = {
'time':[6,7,8,9,10,4,2],
'marks':[60,70,80,90,95,40,20]
    }

df = pd.DataFrame(data)
print(df)

corelation = df['time'].corr(df['marks'])
print(corelation)

plt.scatter(df['marks'],df['time'])
plt.plot(df['time'])
plt.show()
