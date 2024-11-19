import pandas as pd
import numpy as np

data = {
'post_id':[1,2,3,4,5,6,7,8,9,10,11],
'likes':[10,20,30,40,40,50,60,70,10,20,90]
    }

df = pd.DataFrame(data)
print("The data looks as follows:")
print(df)

frequency = df.groupby('likes')['likes'].count()
print("The frquency of the likes as follows : ")
print(frequency)
