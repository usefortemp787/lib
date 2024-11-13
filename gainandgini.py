import csv,math
def read_csv(filename):
    data = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header
        for row in reader:
            data.append(row)
    return data




def Entropy(probs):
    return sum([-p*math.log2(p) for p in probs])

def getEntropy(data,tI):
    vals = [row[tI] for row in data]
    uniqV = set([row[tI] for row in data])
    hashMap = {}
    for v in uniqV:
        hashMap[v] = vals.count(v)
    probs = []
    for vals in hashMap.values():
        probs.append(vals/len(data))
    return Entropy(probs)
        


def Gain(data,aI,tI):
    
    S = getEntropy(data,tI)
    print(S)
    uniqAv = set([row[aI] for row in data])
    wt_ent = 0
    for av in uniqAv:
        subset = [row for row in data if row[aI]==av]
        wt = len(subset)/len(data)
        print(subset)
        ent = getEntropy(subset,tgtI)
        print(wt,ent)
        wt_ent+=(wt*ent)
    return S-wt_ent
        
        
def GiniiND(probs):
    return 1-sum([p**2 for p in probs])      
        
def getGini(data,tI):
    vals = [row[tI] for row in data]
    uniqV = set([row[tI] for row in data])
    hashMap = {}
    for v in uniqV:
        hashMap[v] = vals.count(v)
    probs = []
    for vals in hashMap.values():
        probs.append(vals/len(data))
    return GiniiND(probs)
        
        
def Gini(data,aI,tI):
    uniqAv = set([row[aI] for row in data])
    wt_ent = 0
    for av in uniqAv:
        subset = [row for row in data if row[aI]==av]
        wt = len(subset)/len(data)
        print(subset)
        ent = getGini(subset,tgtI)
        print(wt,ent)
        wt_ent+=(wt*ent)
    return wt_ent
    
    
    









filename = 'data.csv'
data = read_csv(filename)

# Attribute indices
attr_weather = 0  # Weather column
attr_temp = 1     # Temperature column
tgtI = 2          # Target column (Play)

# Calculate Information Gain
info_gain_weather = Gain(data, attr_weather, tgtI)
info_gain_temp = Gain(data, attr_temp, tgtI)

# Output results
print(f"Info Gain for 'Weather': {info_gain_weather:.4f}")
print(f"Info Gain for 'Temperature': {info_gain_temp:.4f}")
gini_weather = Gini(data, attr_weather, tgtI)
gini_tempearture = Gini(data, attr_temp, tgtI)

# Output results
print(f"Gini for 'Weather': {gini_weather:.4f}")
print(f"Gini for 'Temperature': {gini_tempearture:.4f}")