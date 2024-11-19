import numpy as np
import pandas as pd

data = {
'customer_id':[1,2,2,2,1,3,1,3],
'order_date':['2024-01-01','2024-01-02','2024-01-03','2024-01-04','2024-01-05','2024-01-06','2024-01-07','2024-01-08'],
'product_name':['A','B','C','A','A','B','C','B'],
'quantity':[2,1,3,2,4,2,1,3]
    }

df = pd.DataFrame(data)
print("The data is as follows : ")
print(df)

customer_group = df.groupby('customer_id')['product_name'].count()
print("Total number of orders made by the customers are :")
print(customer_group)

product_quantity = df.groupby('product_name')['quantity'].sum()
print("The product average quantity refers as follows : ")
print(product_quantity)

print("The earliest order dates are as follows : ")
earliest_dates = df[df['order_date'] <= '2024-01-05']
print(earliest_dates)



print("The latest order dates are as follows : ")
latest_dates = df[df['order_date'] > '2024-01-02']
print(latest_dates)
