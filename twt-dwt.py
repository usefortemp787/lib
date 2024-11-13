import csv

def read_csv(file):
    data = []
    with open(file,'r') as csvFile: 
        reader = csv.reader(csvFile)
        header = next(reader)
        for row in reader:
            data.append([row[0],int(row[1]),int(row[2]),int(row[3])])
    return data

def twtdwt(data):
    total = {row[0] : {"tv":row[1],"mo":row[2],"tab":row[3]} for row in data}
    sumTv = sum([row[1] for row in data])
    sumMo = sum([row[2] for row in data])
    sumTab = sum([row[3] for row in data])
    
    twt ={}
    dwt={}
    for row in data:
        company,tv,mo,tab = row
        rowTotal = tv+mo+tab
        twt[company] = {"tv":tv/rowTotal,"mo":mo/rowTotal,"tab":tab/rowTotal}
        dwt[company] = {"tv":tv/sumTv,"mo":mo/sumMo,"tab":tab/sumTab}
    return twt,dwt

def TweightDweight(data):
    
    totals = {row[0]: {"tv":0,"mobile":0,"tablet":0} for row in data}
    sumTV = sum([row[1] for row in data])
    sumMobile = sum([row[2] for row in data])
    sumTab = sum([row[3] for row in data])
    twt ={}
    dwt ={}
    for row in data:
        company,tv,mobile,tablet = row
        rTotal = tv+mobile+tablet
        twt[company] = {"tv":tv/rTotal,"mobile":mobile/rTotal,"tablet":tablet/rTotal}
        dwt[company] = {"tv":tv/sumTV,"mobile":mobile/sumMobile,"tablet":tablet/sumTab}
        
        
    return twt,dwt

file = "./test.csv"
data = read_csv(file)
twt,dwt = twtdwt(data)
print(f"{'Company ':<10} {"tv":<10} {"twt_tv":<10} {"dwt_tv":<10} {"mobile":<10} {"twt_mob":<10} {"dwt_mob":<10} {"tab":<10} {"twt_tab":<10} {"dwt_tab":<10} ")
for row in data:
    company,tv,mobile,tablet = row
    print(f"{company:<10} {tv:<10} {round(twt[company]['tv'],2):<10} {round(dwt[company]['tv'],2):<10} {mobile:<10} {round(twt[company]['mo'],2):<10} {round(dwt[company]['mo'],2):<10} {tablet:<10} {round(twt[company]['tab'],2):<10} {round(dwt[company]['tab'],2):<10} ")