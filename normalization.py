import csv,math

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

def write_csv(file_path, headers, data):
    with open(file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        for i in range(len(data[headers[0]])):
            writer.writerow([data[header][i] for header in headers])

def MinMax(data, newMin, newMax):
    oldMin = min(data)
    oldMax = max(data)
    res = []
    for x in data:
        ans = ((x - oldMin) * (newMax - newMin) / (oldMax - oldMin) + newMin )
        res.append(round(ans,3))
    return res

def Zscore(data):
    mean = sum(data) / len(data)
    std_dev = (sum((x - mean) ** 2 for x in data) / len(data)) ** 0.5
    res = []
    for x in data:
        ans = (x-mean)/std_dev
        res.append(round(ans,3))
    return res


def normalize_data(input_file, output_file):
    headers, data = read_csv(input_file)

    for header in headers:
        try:
            col_data = [float(x) for x in data[header]]
        except ValueError:
            continue

        print(f"\nColumn: {header}")
        print("Choose the normalization type:")
        print("1. Min-Max Normalization")
        print("2. Z-Score Normalization")
        choice = input("Enter your choice (1 or 2): ")

        if choice == '1':
            print("Old min value for ",header,": ",min(data[header]))
            print("Old max value for ",header,": ",max(data[header]))
            newMin = float(input(f"Enter new min for {header}: "))
            newMax = float(input(f"Enter new max for {header}: "))
            data[header] = MinMax(col_data, newMin, newMax)
        elif choice == '2':
            print("Old min value for ",header,": ",min(data[header]))
            print("Old max value for ",header,": ",max(data[header]))
            data[header] = Zscore(col_data)
        else:
            print("Invalid choice.")

    write_csv(output_file, headers, data)
    print(f"Normalization complete! Output saved to {output_file}")

if __name__ == "__main__":
    input_file = 'F:\\Final Year Sem 1\\DM\\Assignments\\Assignments\\normalization\\iris.csv'
    output_file = 'normalized_output.csv'

    normalize_data(input_file, output_file)



# def read_csv(file):
#     headers = []
#     data = []
#     with open(file, 'r') as csvfile:
#         csvreader = csv.reader(csvfile)
#         headers = next(csvreader)  # Extract headers (column names)
#         # Initialize list for each column
#         data = [[] for _ in headers]
        
#         for row in csvreader:
#             for i, value in enumerate(row):
#                     data[i].append(float(value))  # Convert to float for numeric columns
    
#     return headers, data

# def write_csv(headers, data, file):
#     with open(file, 'w', newline='') as csvfile:
#         csvwriter = csv.writer(csvfile)
#         csvwriter.writerow(headers)  # Write headers
#         # Write each row of data
#         for row in zip(*data):  # Transpose columns to rows
#             csvwriter.writerow(row)

# def MinMax(data,newMin,newMax):
#     oldMin = min(data)
#     oldMax = max(data)
#     res = []
#     for v in data:
#         ans = (v-oldMin)*(newMax-newMin)/(oldMax-oldMin)+newMin
#         res.append(round(ans,3))
#     return res

# def ZScore(data):
#     mean = round(sum(data)/len(data),3)
#     std = round(math.sqrt(sum([(x-mean)**2 for x in data])/len(data)),3)
#     ans = []
#     for v in data:
#         ans.append(round((v - mean) / std, 3))
#     return ans

# def normalizeAndSave(file):
#     headers,data = read_csv(file)
#     output = []
#     for i in range(len(headers)):
#         print("Select Normalizatioon method : \n")
#         print("1. Min max")
#         print("2. Zscore \n")
#         choice = int(input())
#         if choice == 1:
#             newMin = float(input(f"Enter the new min for {headers[i]}: "))
#             newMax = float(input(f"Enter the new max for {headers[i]}: "))

#             output.append(MinMax(data[i],newMin,newMax))
            
            
#         elif choice == 2:
#             output.append(ZScore(data[i]))
            
#     write_csv(headers, output, "./output.csv")

    
    
# file = './iris.csv'

# normalizeAndSave(file)
            
    
        







