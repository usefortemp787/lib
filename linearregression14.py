import csv
# def mean(values):
#     return sum(values) / len(values)

# def linearRegCoeff1(x, y):
#     n = len(x)
    
#     meanX = mean(x)
#     meanY = mean(y)
    
#     Nr = 0
#     Dr = 0
#     for i in range(n):
#         Nr += (x[i] - meanX) * (y[i] - meanY)
#         Dr += (x[i] - meanX) ** 2
    
#     b1 = Nr / Dr
#     b0 = meanY - b1 * meanX
    
#     return b0, b1

# def read_csv_data(file_path):
#     x = []
#     y = []
    
#     with open(file_path, newline='') as csvfile:
#         reader = csv.reader(csvfile)
#         next(reader)  
        
#         for row in reader:
#             x.append(float(row[0]))  
#             y.append(float(row[1]))  
    
#     return x, y

# def linearRegCoeff12(data):
#     n = len(data)
#     XY = 0
#     X = 0
#     Y = 0
#     X2 = 0

#     for x, y in data:
#         XY += (x * y)
#         X += x
#         Y += y
#         X2 += (x ** 2)

#     denominator = (n * X2) - (X ** 2)

#     m = ((n * XY) - (X * Y)) / denominator
#     c = ((Y * X2) - (X * XY)) / denominator

#     m = round(m, 3)
#     c = round(c, 3)

#     print("Coefficients are b1 : ", m, " b0 : ", c)



# if __name__ == "__main__":
#     file_path = "data.csv"
    
#     x, y = read_csv_data(file_path)
    
#     intercept, slope = linearRegCoeff12(x, y)
#     linearRegCoeff12(list(zip(x,y)))
#     print(f"Intercept (b0): {round(intercept,3)}")
#     print(f"Slope (b1): {round(slope,3)}")



import csv


def read_csv(file):

    x = []
    y = []
    with open(file,'r') as csvFile:
        reader = csv.reader(csvFile)
        next(reader)
        
        for row in reader:
            x.append(float(row[0]))
            y.append(float(row[1]))
    return x,y
            


def coeff(x,y):
    X=0
    Y=0
    X2=0
    XY=0
    n = len(x)
    for i in range(len(x)):
        X+=x[i]
        Y+=y[i]
        X2+=(x[i]**2)
        XY += (x[i]*y[i])
    print(X,Y,XY,X2)
    denr = (n*X2)-(X**2)
    m = ((n*XY)-(X*Y)) / denr
    c = ((Y*X2)-(XY*X)) / denr
    return m,c


file = "./data.csv"
x,y =  read_csv(file)
# print(x,y)
m,c = coeff(x,y)
print("Value of slope m: ",round(m,3))
print("Value of intercept c: ",round(c,3))
print("Equation : y = ",m,"x + ",c)
    
# def read_csv(file):
#     data = []
#     with open(file,'r') as csvFile:
#         reader = csv.reader(csvFile)
#         header = next(reader)
#         for row in reader:
#             data.append([float(row[0]),float(row[1])])
#     return data

# def LinearCoefficient(data):
#     Xcol = [row[0] for row in data]
#     Ycol = [row[1] for row in data]
#     X = sum(Xcol)
#     Y = sum(Ycol)
#     XY = sum([row[0]*row[1] for row in data])
#     X2 = sum([x**2 for x in Xcol])
#     n = len(data)
#     m = (n*XY - X*Y)/(n*X2 - X**2)
#     c = (Y*X2 - X*XY)/(n*X2 - X**2)
#     return m,c


# file = "./data.csv"
# data = read_csv(file)
# print(LinearCoefficient(data))