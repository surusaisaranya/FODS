import numpy as np
import pandas as pd
data = pd.read_csv("C:/Users/Sai Saranya/OneDrive/IT/Bengaluru_House_Data.csv")
print("The review of the data is as follows: ")
print(data)
print(data.columns)
houses_2bath = data[data['bath'] > 2]
print(houses_2bath)
mean = houses_2bath['price'].mean()
print(mean)
