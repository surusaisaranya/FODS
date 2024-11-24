from scipy.stats import ttest_ind
import numpy as np

blood_group = [10,20,30,40,50]
treatment = [55,60,40,10,50]

p_value,t_value = ttest_ind(blood_group,treatment)
print(p_value,t_value)

if (t_value < p_value):
    print("accepted")
else:
    print("no")
