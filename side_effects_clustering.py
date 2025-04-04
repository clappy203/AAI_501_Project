import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Load the dataset
df = pd.read_csv("drug+review+dataset+druglib+com/drugLibTest_raw.tsv", delimiter="\t")

# Encode side effects severity
side_effects_mapping = {
    'No Side Effects': 1,
    'Mild Side Effects': 2,
    'Moderate Side Effects': 3,
    'Severe Side Effects': 4,
    'Extremely Severe Side Effects': 5
}
df['side_effects_encoded'] = df['sideEffects'].map(side_effects_mapping)

# Prepare features for clustering
features = df[['rating', 'side_effects_encoded']].copy()

# Scale the features
scaler = StandardScaler()
scaled_features = scaler.fit_transform(features)

# Perform clustering
kmeans = KMeans(n_clusters=3, random_state=42)
df['side_effect_cluster'] = kmeans.fit_predict(scaled_features)

# Analyze clusters
print("\nCluster Analysis:")
for cluster in range(3):
    cluster_data = df[df['side_effect_cluster'] == cluster]
    print(f"\nCluster {cluster}:")
    print(f"Number of reviews: {len(cluster_data)}")
    print(f"Average rating: {cluster_data['rating'].mean():.2f}")
    print(f"Average side effects severity: {cluster_data['side_effects_encoded'].mean():.2f}")
    print(f"Most common side effects: {cluster_data['sideEffects'].mode()[0]}")

# Visualize clusters
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='rating', y='side_effects_encoded', 
                hue='side_effect_cluster', palette='viridis')
plt.title('Side Effects Clusters')
plt.xlabel('Rating')
plt.ylabel('Side Effects Severity (Encoded)')
plt.savefig('side_effects_clusters.png')
plt.close() 