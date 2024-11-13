import csv,random,math

def read_csv(file):
    data = []
    with open(file,'r') as csvFile:
        reader = csv.reader(csvFile)
        next(reader)
        for row in reader:
            data.append([float(x) for x in row])
    return data

def euclid(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)


def Kmeans(data,k):
    iters = 100
    random.seed(42)
    cntrds = random.sample(data,k)
    for _ in range(iters):
        labels = []
        for point in data:
            mini = float('inf')
            minidx = 0
            for i in range(len(cntrds)):
               dist = euclid(point,cntrds[i])
               if mini>dist:
                   mini = dist
                   minidx = i
            labels.append(minidx)
        
        new_cntrds = []
        
        for j in range(k):
            cluster = [data[x] for x in range(len(data)) if labels[x] == j]
            if cluster :
                newcntrd = []
                for dim in range(len(cluster[0])):
                    dimSum = sum([pt[dim] for pt in cluster])
                    newcntrd.append(dimSum/len(cluster))
                new_cntrds.append(newcntrd)
            else :
                new_cntrds.append[cntrds[j]]
        
        if cntrds == new_cntrds:
            break
        cntrds = new_cntrds
    return labels,cntrds


dataset = read_csv('data.csv')  # Replace with your file path
k = 3  # Number of clusters
labels, centroids = Kmeans(dataset, k)

# Display results
for i, centroid in enumerate(centroids):
    print(f"Centroid {i}: {centroid}")
for i, point in enumerate(dataset):
    print(f"Point {point} is in cluster {labels[i]}")
                    
               
            