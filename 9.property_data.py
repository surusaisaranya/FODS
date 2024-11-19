import pandas as pd
import numpy as np

data = {
"property_id":[1,2,3,4,5,6],
"location":['chennai','hyderabad','banglore','nellore','tirupathi','thirumla'],
'number_of_bedrooms':[8,3,2,1,4,2],
'area':[1200,1300,1100,1000,2000,1200],
'price':[10000,20000,10000,50000,60000,10000]
    }

df = pd.DataFrame(data)
print("The data frame looks as follows : ")
print(df)

average_prices = df.groupby('location')['price'].mean()
print("Average prices in each location refers to:")
print(average_prices)

more_rooms =df[df['number_of_bedrooms'] > 4]
rooms = more_rooms['number_of_bedrooms'].tolist()
print("Properties with more than 4 bed rooms :")
print(more_rooms)

print("The property with the largest area  : ")
sorted_values = df.sort_values('area',ascending = False)
area1 = sorted_values.iloc[0]

print(area1)
