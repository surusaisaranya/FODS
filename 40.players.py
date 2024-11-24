import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("C:/Users/Sai Saranya/Documents/FODS/players.csv")

print("The original dataframe looks as follows:")
print(data)
high_goals = data.sort_values(['goals','salaries'],ascending = False)
print(high_goals)
average_age = data['Ages'].mean()
print("the average age of the players" ,average_age)
result = data[data['Ages'] > average_age]
print(result['Names'])

plt.bar(data['Names'],data['positions'])
plt.show()
