import numpy as np
import pandas as pd
from scipy.stats import t
import math

# Load the data
file_name = "rare_elements.csv"
data = pd.read_csv(file_name)
concentrations = data['concentration']  # Assuming the column is named 'concentration'

# Get user inputs
sample_size = int(input("Enter the sample size: "))
confidence_level = float(input("Enter the confidence level (e.g., 0.95 for 95%): "))
precision = float(input("Enter the desired level of precision (e.g., 0.01 for ±1%): "))

# Take a random sample of the specified size
random_sample = concentrations.sample(n=sample_size, random_state=42)
sample_mean = np.mean(random_sample)
sample_std = np.std(random_sample, ddof=1)

# Calculate the critical t-value
alpha = 1 - confidence_level
t_critical = t.ppf(1 - alpha/2, df=sample_size - 1)

# Calculate margin of error
margin_of_error = t_critical * (sample_std / math.sqrt(sample_size))

# Check if the desired precision is met
if margin_of_error <= precision:
    print("The desired level of precision is met.")
else:
    print("The desired level of precision is NOT met.")
    print(f"Increase the sample size or adjust the precision.")

# Confidence interval
lower_bound = sample_mean - margin_of_error
upper_bound = sample_mean + margin_of_error

# Display results
print(f"\nSample Mean: {sample_mean:.4f}")
print(f"Sample Standard Deviation: {sample_std:.4f}")
print(f"Margin of Error: {margin_of_error:.4f}")
print(f"{confidence_level * 100:.0f}% Confidence Interval: ({lower_bound:.4f}, {upper_bound:.4f})")
