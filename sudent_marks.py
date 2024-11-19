import numpy as np
import pandas as pd

data = {
'math':[90,90,95,97],
'science':[90,90,98,97],
'english':[90,99,98,98],
'history':[89,83,89,90]
    }
df = pd.DataFrame(data)
print(df)
avg_scores = df.mean()
print("Average scores of the subjects",avg_scores)
max_score = avg_scores.max()
print("Maximum score values",max_score)
max_subject = avg_scores.idxmax()
print("Maximum scoring subject",max_subject)
