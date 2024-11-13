import matplotlib.pyplot as plt
import csv

def read_csv_data(filename):
    data = []
    try:
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                if row:
                    data.append(float(row[0]))
    except (FileNotFoundError, ValueError) as e:
        print(f"Error: {e}")
    return data

def calc_stat(data):
    if not data:
        return None

    data_s = sorted(data)
    n = len(data_s)

    minVal = data_s[0]
    maxVal = data_s[-1]

    if n % 2 == 0:
        median = (data_s[n//2 -1] + data_s[n//2])/2
    else:
        median = data_s[n//2]

    lPart = data_s[:n // 2]
    if len(lPart) % 2 == 0:
        q1 = (lPart[len(lPart) // 2 - 1] + lPart[len(lPart) // 2]) / 2
    else:
        q1 = lPart[len(lPart) // 2]

    if n % 2 == 0:
        rPart = data_s[n//2:]
    else:
        rPart = data_s[n//2+1:]
        
    if len(rPart) % 2 == 0:
        q3=(rPart[len(rPart)//2 - 1]+rPart[len(rPart) // 2]) / 2
    else:
        q3=rPart[len(rPart)//2]

    iqr = q3-q1

    return minVal,q1,median,q3,maxVal,iqr



def getStats(data):
    sarr = sorted(data)
    minV = sarr[0]
    maxV = sarr[-1]
    median = 0
    n = len(sarr)
    if n%2 == 0:
        median = (sarr[n//2 -1]+sarr[n//2])/2
    else :
        median = sarr[n//2]
    lpart = sarr[:n//2]
    
    if n%2 == 0:
        rpart = sarr[n//2:]
    else:
        rpart = sarr[n//2+1:]
    
    if len(lpart)%2 == 0:
        q1 = (lpart[len(lpart)//2-1]+lpart[len(lpart)//2])/2
    else :
        q1 = lpart[(len(lpart)//2)]
    if len(rpart) % 2 == 0:
        q3=(rpart[len(rpart)//2 - 1]+rpart[len(rpart) // 2]) / 2
    else:
        q3=rpart[len(rpart)//2]

    iqr = round(q3-q1,3)
    return minV,q1,median,q3,maxV,iqr
        
filename = './iris.csv'
data =read_csv_data(filename)

if data:
    min,q1,median,q3,max,iqr =calc_stat(data)

    lower = q1-1.5*iqr
    upper = q3+1.5*iqr
    outliers = [x for x in data if x < lower or x > upper]

    print(f"Min: {min}, Q1: {q1}, Median: {round(median,3)}, Q3: {q3}, Max: {max}, IQR: {round(iqr,3)}")
    print(getStats(data))
    print(f"Outliers: {outliers}")

    plt.figure(figsize=(8, 6))
    box = plt.boxplot(data, patch_artist=True)

    colors = ['#FF9999']
    for patch in box['boxes']:
        patch.set_facecolor(colors[0])
        patch.set_edgecolor('black')
        patch.set_linewidth(1.5)

    plt.text(1, min, f'Min: {min:.2f}', verticalalignment='bottom', horizontalalignment='right')
    plt.text(1, max, f'Max: {max:.2f}', verticalalignment='top', horizontalalignment='right')
    plt.text(1, q1, f'Q1: {q1:.2f}', verticalalignment='bottom', horizontalalignment='right')
    plt.text(1, q3, f'Q3: {q3:.2f}', verticalalignment='top', horizontalalignment='right')
    plt.text(1, median, f'Median: {median:.2f}', verticalalignment='bottom', horizontalalignment='right')

    for outlier in outliers:
        plt.plot(1, outlier, 'ro') 

    # plt.title('Boxplot of First Column Data with Outliers')
    # plt.xticks([1], ['First Column'])
    # plt.grid(axis='y', linestyle='--', alpha=0.7)
    # plt.show()
else:
    print("Error: No data found in the CSV file.")


# def read_csv(file):
#     data = []
#     with open(file,'r') as csvFile:
#         reader = csv.reader(csvFile)
#         next(reader)
#         for row in reader:
#             data.append(float(row[0]))
            
#     return data


# def write_csv(file,data):
#     with open(file,'w',newline='') as csvFile:
#         writer = csv.writer(csvFile)
#         writer.writerow(["Output"])
#         for row in data:
#             writer.writerow([row])
    
        
    
    

# def getStat(data):
#     sarr = sorted(data)
#     minV = min(sarr)
#     maxV = max(sarr)
#     n = len(sarr)
#     if n%2 == 0:
#         median = (sarr[n//2 -1]+sarr[n//2]) /2
#     else :
#         median = sarr[n//2]
#     lp =[]
#     rp = []
#     if n%2 == 0:
#         lp = sarr[:n//2]
#         rp = sarr[n//2:]
#     else :
#         lp = sarr[:n//2]
#         rp = sarr[n//2+1:]
#     m = len(lp)
#     if len(lp)%2 == 0:
#         q1 = (lp[m//2-1]+lp[m//2])/2
#         q3 = (rp[m//2-1]+rp[m//2])/2
#     else :
#         q1 = (lp[m//2])
#         q3 = (rp[m//2])
        
#     iqr = q3 - q1
    
#     return minV,q1,median,q3,maxV,iqr



# file = './iris.csv'
# data = read_csv(file)
# print(data)
# res = getStat(data)
# ans = []
# for x in res:
#     ans.append(x)
# print(ans)
# write_csv("./output.csv",ans)





    
    