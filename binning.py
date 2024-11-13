import csv
def read_csv(file_path):
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        headers = next(reader)
        data = {header: [] for header in headers}

        for row in reader:
            for i, value in enumerate(row):
                try:
                    data[headers[i]].append(float(value))  
                except ValueError:
                    data[headers[i]].append(value)  

    return headers, data


def BinByMean(arr, n):
    sarr = sorted(arr)
    bin_size = len(sarr) // n
    res = []
    
    for i in range(0,len(sarr),bin_size):
        subarr = arr[i:i+bin_size]
        mean = sum(subarr)/len(subarr)
        tempbin = []
        for _ in range(0,bin_size):
            tempbin.append(round(mean,3))
        res.append(tempbin)
    return res

def BinByBoundary(arr, n):
    sarr = sorted(arr)
    bin_size = len(sarr) // n
    res = []  
    
    for i in range(0, len(sarr), bin_size):
        bin = sarr[i:i + bin_size] 
        binMin = min(bin)
        binMax = max(bin)
        tempbin = []  
        
        for x in bin:
            if abs(x-binMin) < abs(x-binMax):
                tempbin.append(binMin)
            else:
                tempbin.append(binMax)
        
        res.append(tempbin)  
    
    return res

def binBy_Mean(data,n):
    sarr = sorted(data)
    bin_size = len(sarr) // n
    res = []
    for i in range(0,len(sarr),bin_size):
        slist = sarr[i:i+bin_size]
        mean = sum(slist)/len(slist)
        for i in range(0,len(slist)):
            slist[i] = mean
        res.append(slist)
    return res
        
        
def binBy_Boundary(data,n):
    sarr = sorted(data)
    bin_size = len(sarr) // n
    res = []
    for i in range(0,len(sarr),bin_size):
        slist = sarr[i:i+bin_size]
        mini = min(slist)
        maxi = max(slist)
        for i in range(0,len(slist)):
            if abs(slist[i]-mini)<abs(slist[i]-maxi):
                slist[i] = mini
            else :
                slist[i] = maxi
        res.append(slist)
    return res
header,arr = read_csv("data.csv")
arr = arr[header[0]]
n = int(input("Enter the number of bins : "))

binned_mean = BinByMean(arr, n)
print("Binned by mean:", binned_mean)

# print("This is my result : ",binBy_Mean(arr,n))
# print("This is my result boundary : ",binBy_Boundary(arr,n))

binned_boundary = BinByBoundary(arr, n)
print("Binned by boundary:", binned_boundary)


