import numpy as np
import pandas as pd

data = {
'sales':[40,45,50,55,42,46,49,50,53,52,59,60]
    }
df = pd.DataFrame(data)

print("The sales of the whole year is: ")
print(df)

percentage = ((df.sales[3]-df.sales[0])/df.sales[0])*100

print("The percentage of the increasing of the sales is")
print(percentage)
