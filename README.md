
# **PR Assignment-2 on Clustering**
**Course:** IT359 PR  
**Institution:** National Institute of Technology Karnataka (NITK)  
**Submission Date:** [Insert Date]

---

## **1. Data Creation**
### **1.1. Overview**
In this section, I generated a random two-dimensional dataset consisting of 70 data points. The dataset represents points `(xi, yi)` where both `xi` and `yi` are positive integers in the range [1, 99].

### **1.2. Code Implementation**
```python
import random
import matplotlib.pyplot as plt

# Set the number of data points
num_points = 70

# Create a list to hold the data points
dataset = []

# Generate random (xi, yi) points
for _ in range(num_points):
    xi = random.randint(1, 99)
    yi = random.randint(1, 99)
    dataset.append((xi, yi))

# Extract x and y coordinates for plotting
x = [point[0] for point in dataset]
y = [point[1] for point in dataset]

# Plot the points
plt.scatter(x, y)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Scatter Plot of Random Dataset')
plt.grid(True)
plt.show()
```

### **1.3. Assumptions**
- **Range of Values**: The dataset was generated with both `xi` and `yi` constrained between 1 and 99, ensuring a uniform spread across the 2D space.
- **Number of Points**: A minimum of 70 points was selected to provide a sufficiently complex dataset for clustering.

### **1.4. Key Learnings**
- Learned how to create and visualize a 2D dataset for clustering purposes.
- Realized the importance of randomness in generating test data to simulate real-world scenarios.

---

## **2. K-Means Clustering Algorithm**
### **2.1. Overview**
The K-Means clustering algorithm was implemented to group the dataset into clusters based on Euclidean distance. The value of `k` was assumed to be 3, based on the spread and visual observation of the dataset.

### **2.2. Code Implementation**
```python
import random
import numpy as np
import matplotlib.pyplot as plt

# Function to calculate Euclidean distance
def euclidean_distance(p1, p2):
    return np.sqrt(np.sum((p1 - p2) ** 2))

# K-means algorithm
def k_means(dataset, k, max_iterations=100):
    # Randomly initialize the centroids by selecting k random points from the dataset
    centroid_indices = random.sample(range(len(dataset)), k)
    centroids = dataset[centroid_indices]
    
    for _ in range(max_iterations):
        # Create a list of empty clusters
        clusters = [[] for _ in range(k)]
        
        # Assign each data point to the nearest centroid
        for point in dataset:
            distances = [euclidean_distance(point, centroid) for centroid in centroids]
            closest_centroid = np.argmin(distances)
            clusters[closest_centroid].append(point)
        
        # Calculate new centroids as the mean of the clusters
        new_centroids = [np.mean(cluster, axis=0) if cluster else centroids[i] for i, cluster in enumerate(clusters)]
        
        # Check for convergence (if centroids don't change)
        if np.allclose(new_centroids, centroids):
            break
        
        centroids = new_centroids
    
    return clusters, centroids

# Function to calculate SSE (Sum of Squared Errors) for a cluster
def calculate_sse(cluster, centroid):
    return np.sum([euclidean_distance(point, centroid) ** 2 for point in cluster])

# Function to calculate scatter coefficient
def calculate_scatter(clusters, centroids):
    # Calculate intra-cluster SSE
    intra_cluster_sse = sum([calculate_sse(clusters[i], centroids[i]) for i in range(len(clusters))])
    
    # Calculate the global centroid (mean of all data points)
    global_centroid = np.mean([point for cluster in clusters for point in cluster], axis=0)
    
    # Calculate inter-cluster SSE
    inter_cluster_sse = sum([len(cluster) * euclidean_distance(centroid, global_centroid) ** 2 
                             for cluster, centroid in zip(clusters, centroids)])
    
    # Calculate scatter coefficient
    scatter = intra_cluster_sse / inter_cluster_sse
    return scatter

# Set the number of clusters
k = 3

# Apply K-means clustering
clusters, centroids = k_means(dataset, k)

# Calculate scatter coefficient
scatter = calculate_scatter(clusters, centroids)
print(f"Scatter coefficient: {scatter}")

# Plotting the clusters
colors = ['r', 'g', 'b']
for i, cluster in enumerate(clusters):
    cluster = np.array(cluster)
    plt.scatter(cluster[:, 0], cluster[:, 1], c=colors[i])
plt.scatter(np.array(centroids)[:, 0], np.array(centroids)[:, 1], c='y', marker='x')
plt.title('K-means Clustering')
plt.show()
```

### **2.3. Assumptions**
- **Value of K**: The value of `k` was assumed to be 3, based on an initial visual inspection of the dataset. This assumption allowed for clear distinctions between clusters while minimizing intra-cluster SSE.
- **Stopping Criteria**: The algorithm was set to stop when the centroids no longer change significantly between iterations.

### **2.4. Key Learnings**
- Understood the K-Means algorithm, particularly the process of centroid updating and convergence.
- Learned how to calculate the scatter coefficient, a key metric for evaluating cluster quality.
- Gained insight into the significance of choosing an appropriate `k` value.

---

## **3. Agglomerative Hierarchical Clustering (AHC) - Using `scipy`**
### **3.1. Overview**
Agglomerative Hierarchical Clustering (AHC) was first implemented using the `scipy` library's built-in functions, with Manhattan distance as the distance measure. A dendrogram was used to visualize the hierarchical structure of the clusters.

### **3.2. Code Implementation**
```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage

# Prepare for dendrogram plotting using linkage method
Z = linkage(dataset, method='complete', metric='cityblock')  # Cityblock is Manhattan distance

# Plotting the dendrogram
plt.figure(figsize=(10, 7))
dendrogram(Z)
plt.title('Agglomerative Hierarchical Clustering (Manhattan Distance)')
plt.xlabel('Data Points')
plt.ylabel('Distance')
plt.show()
```

### **3.3. Assumptions**
- **Manhattan Distance**: Manhattan distance was chosen as it is more robust to outliers and scales better with high-dimensional data compared to Euclidean distance.
- **Complete Linkage**: Complete linkage was used, which considers the maximum distance between points in different clusters when determining which clusters to merge.

### **3.4. Key Learnings**
- Learned how to use the `scipy` library for AHC, particularly the `linkage` and `dendrogram` functions.
- Understood the hierarchical structure of clustering and the significance of linkage methods.
- Gained insight into the interpretability of dendrograms for visualizing cluster formations.

---

## **4. Agglomerative Hierarchical Clustering (AHC) - Custom Implementation**
### **4.1. Overview**
Given the assignment's requirement to avoid special-purpose libraries, a custom implementation of AHC was developed. This approach involved manually calculating the Manhattan distances and creating a dendrogram based on the distance matrix.

### **4.2. Code Implementation**
```python
import numpy as np
import matplotlib.pyplot as plt

# Function to calculate Manhattan distance between two points
def manhattan_distance(p1, p2):
    return np.sum(np.abs(p1 - p2))

# Initialize each data point as its own cluster
clusters = [[i] for i in range(len(dataset))]

# Create a distance matrix
distance_matrix = np.zeros((len(dataset), len(dataset)))

for i in range(len(dataset)):
    for j in range(len(dataset)):
        distance_matrix[i][j] = manhattan_distance(dataset[i], dataset[j])

# List to store the dendrogram steps
dendrogram_steps = []

while len(clusters) > 1:
    min_dist = float('inf')
    to_merge = None

    for i in range(len(clusters)):
        for j in range(i + 1, len(clusters)):
            dist = np.min([distance_matrix[p1][p2] for p1 in clusters[i] for p2 in clusters[j]])
            if dist < min_dist:
                min_dist = dist
                to_merge = (i, j)

    cluster1, cluster2 = to_merge
    new_cluster = clusters[cluster1] + clusters[cluster2]
    dendrogram_steps.append((clusters[cluster1], clusters[cluster2], min_dist))
    clusters.append(new_cluster)
    clusters.pop(max(cluster1, cluster2))
    clusters.pop(min(cluster1, cluster2))

# Function to plot the dendrogram
def plot_dendrogram(dendrogram_steps, num_points):
    plt.figure(figsize=(10, 7))
    x_current = np.arange(num_points)
    cluster_positions = {i: x for i, x in enumerate(x_current)}

    for

 step, (cluster1, cluster2, dist) in enumerate(dendrogram_steps):
        y = [step + 1] * 2
        x1 = np.mean([cluster_positions[p] for p in cluster1])
        x2 = np.mean([cluster_positions[p] for p in cluster2])

        plt.plot([x1, x1, x2, x2], [step, y[0], y[1], step], c='b')
        cluster_positions[step + num_points] = (x1 + x2) / 2

    plt.xlabel('Data Points')
    plt.ylabel('Distance')
    plt.title('Custom AHC Dendrogram')
    plt.show()

plot_dendrogram(dendrogram_steps, len(dataset))
```

### **4.3. Assumptions**
- **Manhattan Distance**: This was chosen to ensure consistency with the `scipy` implementation.
- **Distance Matrix Calculation**: The distance matrix was calculated manually to facilitate the custom implementation of the AHC algorithm.
- **Merge Strategy**: At each step, the two closest clusters (in terms of minimum distance) were merged.

### **4.4. Key Learnings**
- Gained a deep understanding of the AHC process, particularly the iterative merging of clusters based on distance.
- Realized the importance of distance metrics in determining cluster formations.
- Learned how to manually implement and visualize a dendrogram, reinforcing the concepts of hierarchical clustering.

---

## **Conclusion**
This report detailed the process of data creation, implementation of K-Means clustering, and two approaches to Agglomerative Hierarchical Clustering (AHC). The project reinforced key concepts of clustering algorithms, such as centroid updating, distance metrics, and the significance of dendrograms in understanding hierarchical structures.

**Key Learnings**:
- The critical role of assumptions, such as the choice of distance metric, in determining the performance of clustering algorithms.
- The importance of visualizations, such as scatter plots and dendrograms, in interpreting and evaluating clustering results.
- A deeper understanding of both library-based and custom implementations of clustering algorithms.
