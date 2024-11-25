import numpy as np
import pandas as pd

data = {

"cust_id":[1,2,3,4,5],
"reviews":["good","bad","good","worst","bad"]
    }

df = pd.DataFrame(data)
print("The data will look like this : ")
print(df)

grouped_data = df.groupby('reviews')['reviews'].count()
print("The frequency of the grouped data looks like as follows :")
print(grouped_data)
