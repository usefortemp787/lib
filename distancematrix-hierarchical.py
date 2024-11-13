import csv

def read_lower_triangular(file):
    distMat = []
    with open(file, 'r') as csvFile:
        reader = csv.reader(csvFile)
        for row in reader:
            distMat.append([float(value) for value in row])
    n = len(distMat)
    tdistMat = [[0 for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(0,i+1):
            tdistMat[i][j] = distMat[i][j]
            tdistMat[j][i] = tdistMat[i][j]
    return tdistMat

def findClosestClusters(distMat):
    n = len(distMat)
    min_dist = float('inf')
    closest_pair = (0, 0)
    
    for i in range(1, n):
        for j in range(i):
            if distMat[i][j] < min_dist:
                min_dist = distMat[i][j]
                closest_pair = (i, j)
                
    return closest_pair

def updateDistMat(distMat, c1, c2):
    n = len(distMat)
    
    # Update the distances for cluster `c1` by taking the minimum distances with `c2`
    for i in range(n):
        if i != c1 and i != c2:
            # Take the minimum distance between `c1` and `c2` for the current index
            distMat[c1][i] = min(distMat[c1][i], distMat[c2][i])
            distMat[i][c1] = distMat[c1][i]  # Ensure symmetry in the matrix

    # Remove the row and column for `c2` safely
    del distMat[c2]  # Remove the row for `c2`
    for row in distMat:
        del row[c2]  # Remove the column for `c2`
    
    return distMat



def Hierarchical_Clustering(distMat):
    n = len(distMat)
    clusters = [[i] for i in range(n)]
    
    while len(clusters) > 1:
        # Find the closest clusters
        c1, c2 = findClosestClusters(distMat)
        
        # Merge clusters
        new_cluster = clusters[c1] + clusters[c2]
        min_ind, max_ind = min(c1, c2), max(c1, c2)
        
        # Update the clusters list
        clusters[min_ind] = new_cluster
        del clusters[max_ind]
        print(clusters)
        # Update the distance matrix
        distMat = updateDistMat(distMat, c1, c2)
        
    return clusters

file = "./test.csv"
distMat = read_lower_triangular(file)
print("Initial Distance Matrix:", distMat)
print("Final Clusters:", Hierarchical_Clustering(distMat))
