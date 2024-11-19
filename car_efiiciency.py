import numpy as np
import pandas as pd

data = {
'fuel_efficiency':[50,90,89,78,90,89,34,56,78],
'car_model':['A','B','C','A','B','C','A','B','C']
    }


df =pd.DataFrame(data)
print("The reviewd data for the car effiency is:")
print(df)

grouped_cars = df.groupby('car_model')['fuel_efficiency'].mean()
print(grouped_cars)


for i in range(len(grouped_cars)-1):
               efficiency = ((grouped_cars.iloc[i+1] - grouped_cars.iloc[i])/grouped_cars.iloc[i])*100
               print("The model efficiency between ",i,"and",i+1,"is",efficiency)
