import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Sample dataset (replace with actual data)
data = {
    'Customer ID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Total Amount Spent': [500, 600, 800, 200, 300, 1200, 700, 400, 900, 1000],
    'Frequency of Visits': [10, 12, 15, 5, 7, 20, 18, 8, 22, 25]
}

# Convert data into a DataFrame
df = pd.DataFrame(data)

# Select features for clustering
X = df[['Total Amount Spent', 'Frequency of Visits']]

# Normalize the data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Determine the optimal number of clusters using the Elbow Method
wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, random_state=42)
    kmeans.fit(X_scaled)
    wcss.append(kmeans.inertia_)

# Plot the Elbow Method
plt.figure(figsize=(8, 5))
plt.plot(range(1, 11), wcss, marker='o')
plt.title('Elbow Method to Determine Optimal Clusters')
plt.xlabel('Number of Clusters')
plt.ylabel('WCSS')
plt.grid()
plt.show()

# Fit the K-Means model (using 3 clusters as an example)
kmeans = KMeans(n_clusters=3, random_state=42)
df['Cluster'] = kmeans.fit_predict(X_scaled)

# Visualize the clusters
plt.figure(figsize=(10, 6))
sns.scatterplot(
    x=df['Total Amount Spent'],
    y=df['Frequency of Visits'],
    hue=df['Cluster'],
    palette='viridis',
    s=100
)
plt.title('Customer Segments')
plt.xlabel('Total Amount Spent')
plt.ylabel('Frequency of Visits')
plt.legend(title='Cluster')
plt.grid()
plt.show()

# Insights
print("\nCluster Analysis:")
for cluster in df['Cluster'].unique():
    cluster_data = df[df['Cluster'] == cluster]
    print(f"\nCluster {cluster}:")
    print(f"Average Spending: {cluster_data['Total Amount Spent'].mean():.2f}")
    print(f"Average Frequency: {cluster_data['Frequency of Visits'].mean():.2f}")
