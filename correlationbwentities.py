import csv

# def read_csv(filename):
#     dataset = []
#     with open(filename, 'r') as file:
#         reader = csv.reader(file)
#         next(reader)  # Skip the header
#         for row in reader:
#             dataset.append([int(value) for value in row])  # Convert values to integers (0 or 1)
#     return dataset

# def probability(ec):
#     return sum(ec) / len(ec)

# def jointProb(ec_A, ec_B):
#     count = 0
#     for a, b in zip(ec_A, ec_B):
#         if a == 1 or b == 1:
#             count += 1
#     return count / len(ec_A)

# def correlation(ec_A, ec_B):
#     P_A = probability(ec_A)
#     P_B = probability(ec_B)
#     P_A_union_B = jointProb(ec_A, ec_B)
    
#     if P_A * P_B == 0:  
#         return 0
    
#     return P_A_union_B / (P_A * P_B)

# def calcCorrMat(dataset):
#     num_columns = len(dataset[0]) 
#     correlation_matrix = []
    
#     for i in range(num_columns):
#         row = []
#         for j in range(num_columns):
#             if i == j:
#                 row.append(1)  
#             else:
#                 column_i = [row[i] for row in dataset]
#                 column_j = [row[j] for row in dataset]
#                 correlation = correlation(column_i, column_j)
#                 row.append(correlation)
#         correlation_matrix.append(row)
    
#     return correlation_matrix

# def print_correlation_matrix(matrix):
#     for row in matrix:
#         print(row)

# filename = 'data.csv' 
# dataset = read_csv(filename)
# correlation_matrix = calcCorrMat(dataset)
# print_correlation_matrix(correlation_matrix)


def read_csv(file):
    data = []
    with open(file,'r') as csvFile:
        reader = csv.reader(csvFile)
        header = next(reader)
        for row in reader:
            data.append([float(i) for i in row])
    return data

def PearsonCoefficient(data):
    X = [row[0] for row in data]
    Y = [row[1] for row in data]
    Ymean = sum(Y) / len(Y)
    Xmean = sum(X) / len(X)
    n = len(data)
    Cov_X_Y = sum([(row[1] - Ymean)*(row[0] - Xmean) for row in data]) / n
    Std_x = (sum([(row[0] - Xmean)**2 for row in data]) / n)**0.5
    Std_y = (sum([(row[1] - Ymean)**2 for row in data]) / n)**0.5
    
    return Cov_X_Y/(Std_x*Std_y)


file = "./data.csv"
print("Correlation between X and Y columns : ",PearsonCoefficient(read_csv(file)))