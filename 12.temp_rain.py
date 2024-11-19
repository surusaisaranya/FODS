import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
data = {

'month':['Jan','Feb','Mar','Apr','May','Jun','July','Aug','Sept','Oct'],
'temp':[35,36,90,38,39,20,41,42,43,44],
'rainfall':[10,20,30,40,90,60,70,80,90,100]

    }

df = pd.DataFrame(data)
print("The data Frame looks like : ")
print(df)


plt.plot(df['month'],df['temp'],color = 'red' , label = 'Temperature')
plt.xlabel("Months")
plt.ylabel("Temperature")
plt.show()

plt.scatter(df['month'],df['rainfall'],color = 'blue' , label = 'rain fall')
plt.xlabel("Months")
plt.ylabel("Rainfall")
plt.show()
