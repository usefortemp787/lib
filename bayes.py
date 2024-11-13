import csv


def read_csv(file):
    data =[]
    with open(file,'r') as csvFile:
        reader = csv.reader(csvFile)
        header = next(reader)
        for row in reader:
            data.append(row)
    return header,data


def calcPrio(data,tgtI,tgtV):
    c = sum([1 if row[tgtI]==tgtV else 0 for row in data])
    return round(c/len(data),3)

def Prob(data,fI,fV,tgtI,tgtV):
    ct = 0
    cft = 0
    for row in data:
        if row[tgtI] == tgtV and row[fI]==fV:
            cft+=1
        if row[tgtI] == tgtV:
            ct+=1
    return round(cft/ct,3)
            

def Bayes(data,newInp,tgtI):
    res = {}
    uniqTgtV = set([row[tgtI] for row in data])
    for tgtV in uniqTgtV:
        prior_prob = calcPrio(data,tgtI,tgtV)
        print("P(",tgtV,") = ",prior_prob)
        for i in range(len(newInp)):
            cond = Prob(data,i,newInp[i],tgtI,tgtV)
            print("P(",newInp[i],"/",tgtV,") = ",cond)
            prior_prob *=cond
        
        print("P(",newInp,"/",tgtV,") = ",round(prior_prob,3))
        res[tgtV] = round(prior_prob,3)
    return max(res,key=res.get)
    
    
file ="./data.csv"
header,data = read_csv(file)
print("Output is : ",Bayes(data,["Sunny", "Hot", "High", "False"],4))