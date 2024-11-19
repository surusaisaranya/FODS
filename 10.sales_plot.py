import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = {

'month':[1,2,3,4,5,6,7,8,9,10,11,12],
'sales':[78,79,80,85,89,90,88,89,80,78,72,69]
    }
df = pd.DataFrame(data)
print("\n\n\n The data looks as follows :")
print(df)

plt.scatter(df['month'],df['sales'],color = 'blue')
plt.plot(df['sales'],color = "red")
plt.xlabel("Months of the sales")
plt.ylabel("Sales of each month")
plt.title("Sales in moth wise in a year")
plt.show()


plt.bar(df['month'],df['sales'])
plt.xlabel("Months of the sales")
plt.ylabel("Sales of each month")
plt.title("Sales in moth wise in a year")
plt.show()
