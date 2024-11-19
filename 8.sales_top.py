import numpy as np
import pandas as pd

data = {

'month':[1,2,3,4,5,6,7,8,9,10,11,12],
'sales':[57,67,89,87,67,69,75,69,74,56,59,79],
'product_names':['a','b','c','b','e','b','e','b','a','b','c','b']
    }

df = pd.DataFrame(data)
print("The data frame is as follows : ")
print(df)

print("The sales in the descending order is : ")
top_sales = df.sort_values('sales',ascending = False)
print(top_sales)

print("The top 5 sales from the year is :")
print(top_sales.head(5))

print("The product names that sold in the last year are : ")
print(set(top_sales.head(5)['product_names'].tolist()))
