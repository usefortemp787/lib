# import csv
# import math

# # Step 1: Reading data from the CSV file and converting it to a list of lists (dataset)
# def read_csv(filename):
#     dataset = []
#     with open(filename, 'r') as file:
#         reader = csv.reader(file)
#         next(reader)  # Skip the header
#         for row in reader:
#             dataset.append([float(value) for value in row])  # Convert values to float
#     return dataset

# # Step 2: Calculating the Euclidean distance between two points
# def euclidDist(p1, p2):
#     return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# # Step 3: Compute distance matrix for the dataset
# def compute_dist_mat(dataset):
#     n = len(dataset)
#     dist_mat = [[0] * n for _ in range(n)]  # Create an empty n x n matrix
#     for i in range(n):
#         for j in range(i + 1, n):
#             dist = euclidDist(dataset[i], dataset[j])  # Compute distance
#             dist_mat[i][j] = round(dist, 2)  # Symmetric distance matrix
#             dist_mat[j][i] = round(dist, 2)
#     return dist_mat

# def computeDistMat(data):
#     distMat = [[0 for j in range(len(data))] for i in range(len(data))]
#     n = len(data)
#     for i in range(n):
#         for j in range(n):
#             dist = euclidDist(data[i],data[j])
#             distMat[i][j]=dist
#             distMat[j][i]=dist
#     # print(distMat)
#     return distMat

# def FindClosestCluster(distMat):
#     mini = float('inf')
#     res = [0,0]
#     for i in range(len(distMat)):
#         for j in range(i+1,len(distMat)):
#             if mini > distMat[i][j]:
#                 mini = distMat[i][j]
#                 res[0]=i
#                 res[1]=j
#     return res
    
# def updateDistMattt(distMat,c1,c2):
#     n = len(distMat)
#     tdistMat = [[distMat[i][j] for j in range(n)] for i in range(n)]
#     for i in range(n):
#         if i not in (c1,c2):
#             tdistMat[i][c1] = min(distMat[i][c1],distMat[i][c2])
#             tdistMat[c1][i] = tdistMat[i][c1]
#     del tdistMat[c2]
#     for row in tdistMat:
#         del row[c2]      
#     return tdistMat
    
# def HierarchicalClustering(data):
#     distMat = computeDistMat(data)
#     clusters = [[i] for i in range(len(data))]
#     while len(clusters)>1:
#         c1,c2 = FindClosestCluster(distMat)
#         newC = clusters[c1]+clusters[c2]
        
#         clusters.append(newC)
        
#         del clusters[max(c1,c2)]
#         del clusters[min(c1,c2)]
#         print("( ",data[c1],data[c2] ," ) => ",newC ," = >",clusters)
#         distMat = updateDistMat(distMat,c1,c2)
#     return clusters

# # Step 4: Find the closest pair of clusters from the distance matrix
# def find_closest_clusters(dist_mat):
#     min_dist = float('inf')
#     cluster_pair = (0, 1)
#     n = len(dist_mat)
#     for i in range(n):
#         for j in range(i + 1, n):
#             if dist_mat[i][j] < min_dist:
#                 min_dist = dist_mat[i][j]
#                 cluster_pair = [i, j]
#     return cluster_pair

# # Step 5: Merge two clusters
# def merge(cluster1, cluster2):
#     return cluster1 + cluster2

# # Step 6: Update the distance matrix after merging clusters for single linkage
# def updateDistMat(dist_mat, cluster1, cluster2):
#     n = len(dist_mat)
#     new_dist_mat = [[dist_mat[i][j] for j in range(n)] for i in range(n)]  # Copy the original matrix

#     for i in range(n):
#         if i not in (cluster1, cluster2):
#             # Use min for single linkage
#             new_dist_mat[i][cluster1] = min(dist_mat[i][cluster1], dist_mat[i][cluster2])  # Min distance
#             new_dist_mat[cluster1][i] = new_dist_mat[i][cluster1]  # Ensure symmetry

#     # Remove the row and column for cluster2 as it is merged with cluster1
#     del new_dist_mat[cluster2]  
#     for row in new_dist_mat:
#         del row[cluster2]  

#     return new_dist_mat

# # Step 7: Main function to perform hierarchical clustering
# def hierarchical_clustering(dataset):
#     dist_mat = compute_dist_mat(dataset)
#     clusters = [[i] for i in range(len(dataset))]  # Start with each data point as a cluster
#     print("Clusters : ",clusters)
#     iteration = 1
#     while len(clusters) > 1:
#         cluster1, cluster2 = find_closest_clusters(dist_mat)  # Find the closest clusters
#         new_cluster = merge(clusters[cluster1], clusters[cluster2])  # Merge the clusters
        
#         print(f"Iter {iteration}: Merging clusters {clusters[cluster1]} and {clusters[cluster2]} into {new_cluster}")
        
#         clusters.append(new_cluster)  # Add the new cluster
#         del clusters[max(cluster1, cluster2)]  # Remove merged clusters
#         del clusters[min(cluster1, cluster2)]
        
#         dist_mat = updateDistMattt(dist_mat, cluster1, cluster2)  # Update the distance matrix
#         iteration += 1

#     print(f"\nFinal cluster: {clusters[0]}")
#     return clusters[0]

# # Step 8: Run the code by reading a CSV file and performing clustering
# if __name__ == "__main__":
#     filename = './data.csv'  # File path
#     data = read_csv(filename)  # Load the dataset
#     clusters = HierarchicalClustering(data)  # Perform clustering
#     print("Printing")
#     # print(computeDistMat(data))
#     print(clusters)  # Print the final cluster



# import math,csv

# def read_csv(filename):
#     dataset = []
#     with open(filename, 'r') as file:
#         reader = csv.reader(file)
#         next(reader)  # Skip the header
#         for row in reader:
#             dataset.append([float(value) for value in row])  # Convert values to float
#     return dataset

# def euclidDist(p1,p2):
#     return math.sqrt((p2[1]-p1[1])**2 + (p2[0]-p1[0])**2)

# def createDistMat(data):
#     distMat = [[0 for j in range(len(data))] for i in range(len(data))]
#     n = len(data)
#     for i in range(n):
#         for j in range(i+1,n):
#             dist = euclidDist(data[i],data[j])
#             distMat[i][j]=distMat[j][i]= dist
#     return distMat


# def findClosestCluster(distMat):
#     mini = float('inf')
#     res = [0,0]
#     for i in range(len(distMat)):
#         for j in range(i+1,len(distMat)):
#             if distMat[i][j]<mini:
#                 mini = distMat[i][j]
#                 res[0]=i
#                 res[1]=j
#     return res


# def updateDistMat(distMat,c1,c2):
#     n = len(distMat)
#     tdistMat = [[distMat[i][j] for j in range(n)] for i in range(n)]
#     for i in range(n):
#         if i not in (c1,c2):
#             tdistMat[i][c1] = min(tdistMat[i][c1],tdistMat[i][c2])
#             tdistMat[c1][i] = tdistMat[i][c1]
#     del tdistMat[c2]
#     for row in tdistMat:
#         del row[c2]
#     return tdistMat
        



# def hierarchicalClustering(data):
#     distMat = createDistMat(data)
#     clusters = [[i] for i in range(len(data))]
#     while(len(clusters)>1):
#         c1,c2 = findClosestCluster(distMat)
#         newC = clusters[c1]+clusters[c2]
#         clusters.append(newC)
#         del clusters[max(c1,c2)]
#         del clusters[min(c1,c2)]
#         distMat = updateDistMat(distMat,c1,c2)
#     return clusters



# filename = './data.csv'  # File path
# data = read_csv(filename)  # Load the dataset
# clusters = hierarchicalClustering(data)  # Perform clustering
# print("Printing")
# # print(computeDistMat(data))
# print(clusters)  # Print the final cluster











import csv,math


def read_csv(file):
    data = []
    with open(file,'r') as csvFile:
        reader = csv.reader(csvFile)
        header = next(reader)
        for row in reader:
            data.append([float(i) for i in row])
    return header,data

def euclidean(p1,p2):
    return math.sqrt((p2[1]-p1[1])**2 + (p2[0]-p1[0])**2)

def createDistMat(data):
    n = len(data)
    distMat = [[0 for j in range(n)]for i in range(n)]
    for i in range(len(data)):
        for j in range(i+1,n):
            dist = euclidean(data[i],data[j])
            distMat[i][j] = round(dist,3)
            distMat[j][i] = round(dist,3)
    return distMat


def findClosestCluster(distMat):
    print("dist-matrix : ")
    for row in distMat:
        print(row)
    mini = float('inf')
    res = [0,0]
    for i in range(len(distMat)):
        for j in range(i+1,len(distMat)):
            if distMat[i][j]<mini:
                mini = distMat[i][j]
                res[0] = i
                res[1] = j
    print("mindist",distMat[res[0]][res[1]])
    return res
          
def updateDistMat(distMat,c1,c2):
    n = len(distMat)
    tDistMat = [[distMat[i][j] for j in range(n)] for i in range(n)]
    for i in range(n):
        if i not in (c1,c2):
            tDistMat[i][c1] = min(tDistMat[i][c1],tDistMat[i][c2])
            tDistMat[c1][i] = tDistMat[i][c1]
    del tDistMat[c2]
    for row in tDistMat:
        del row[c2]
    return tDistMat
          
def HierarchicalClustering(data):
    distMat = createDistMat(data)
    clusters = [[i] for i in range(len(data))]  # index-based clustering
    while len(clusters) > 1:
        c1, c2 = findClosestCluster(distMat)
        
        newC = clusters[c1] + clusters[c2]
        
        min_idx = min(c1, c2)
        max_idx = max(c1, c2)
        d1 = [tuple(data[idx]) for idx in clusters[c1]]
        d2 = [tuple(data[idx]) for idx in clusters[c2]]
        del clusters[max_idx]  # Remove the cluster at max index first to avoid shifting
        del clusters[min_idx]  # Remove the cluster at min index
       
        clusters.insert(min_idx, newC)  # Insert the new cluster at the original min index
        print("Cluster index ",clusters)
        distMat = updateDistMat(distMat, c1, c2)
        
        
        
        vis = []
        for cluster in clusters:
            vis.append([tuple(data[idx]) for idx in cluster])
        
        print(d1, " + ", d2, " => ", vis, end="\n\n")
                
    return clusters


file = "./data.csv"
header,data = read_csv(file)
print(HierarchicalClustering(data))


