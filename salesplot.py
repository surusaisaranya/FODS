import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
data = {
'Date':['2024-10-01','2024-10-02','2024-10-03','2024-10-04','2024-10-05'],
'Price':[100,900,8990,456,890]
    }
df = pd.DataFrame(data)
print(df)
df['Date']=pd.to_datetime(df['Date'])
plt.plot(df['Date'],df['Price'])
plt.xlabel('Date')
plt.ylabel('Prices')
plt.show()
