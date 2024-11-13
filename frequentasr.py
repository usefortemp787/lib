import csv
from itertools import combinations

def read_csv(file):
    txns = []
    items = ["Milk","Bread","Butter","Ketchup","Cookies","Egg"]
    with open(file,'r') as csvFile:
        reader = csv.reader(csvFile)
        for row in reader : 
            txns.append([1 if item in row else 0 for item in items])
    return items,txns


def generateItemset(n,size):
    return list(combinations(range(n),size))


def Support(itemset,txns):
    
    c = 0
    for txn in txns : 
        s = 0
        for item in itemset:
            if txn[item] == 1:
                s+=1
        if s == len(itemset):
            c+=1
    return c/len(txns)

def Apriori(txns,items,minSupp):
    all_f_itemsets = []
    afi =[]
    n = len(items)
    for size in range(1,n+1):
        itemsets = generateItemset(n,size)
        f_itemsets = []
        for itemset in itemsets:
            supp = Support(itemset,txns)
            if supp>=minSupp:
                afi.append([itemset,supp])
                modi = [items[item] for item in itemset]
                f_itemsets.append([modi,supp])
        if not f_itemsets:
            break
        all_f_itemsets.extend(f_itemsets)
    return all_f_itemsets,afi


def Confidence(S,I_minus_S,txns):
    return Support(S+I_minus_S,txns)/Support(S,txns)

def generateASR (txns,items,afi,minconf):
    rules = []
    for fi,supp in afi :
        if len(fi)>1 :
            for i in range(1,len(fi)+1):
                for subset in combinations(range(len(fi)),i) :
                    S = list(subset)
                    I_minus_S = [item for item in fi if item not in S]
                    print(S,I_minus_S)
                    if I_minus_S :
                        conf =Confidence(S,I_minus_S,txns)
                        if minconf<=conf:
                            fin1 = [items[i] for i in S]
                            fin2 = [items[i] for i in I_minus_S]
                            rules.append([fin1, fin2, conf])
    return rules
                    
             
    
    
file = './data.csv'
items,txns = read_csv(file)

fi ,afi = Apriori(txns,items,0.5)
rules = generateASR(txns,items,afi,0.4)
def write_csv(file,data,asrdata):
    with open(file,'w',newline='') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(['Itemsets','Support'])
        for row in data:
            writer.writerow(row)
        writer.writerow(['\n'])
        writer.writerow(['Rule','Confidence'])
        for row in asrdata:
            writer.writerow(row)
        
            
write_csv("./output6.csv",fi,rules)