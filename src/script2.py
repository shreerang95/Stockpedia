# script to store normalized percentage change (percentage change / max percentage change over 2 years) of S&P 500 index for each day

import csv
file_data=[]
max=0.0
min=0.0
with open('../Data/GSPC_RAW_change_1.csv','r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ',')
    for row in csv_reader:
        if(float(row[5])>0.0):
            if(float(row[5])>max):
                max=float(row[5])
        if(float(row[5])<0.0):
            if(float(row[5])<min):
                min=float(row[5])
        row.append(0.0)
        file_data.append(row)
    # for i in file_data:
    #     print(i)

# print(file_data)

for i in range(len(file_data)):

    if(float(file_data[i][5])>0.0):
        file_data[i][6] = float(file_data[i][5]) / max
    else:
        file_data[i][6] = float(file_data[i][5]) / min

# print(file_data)

with open('../Data/GSPC_RAW_change_1.csv','w') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter = ',')
    csv_writer.writerows(file_data)

csv_file.close()