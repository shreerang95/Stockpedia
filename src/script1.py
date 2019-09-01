# script to stor percentage change f S&P 500 index for each day

import csv

file_data=[]

with open('../Data/GSPC1.csv','r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ',')
    for row in csv_reader:
        if(row[0] == 'Date'):
            file_data.append(row)
            continue
        row[5] = ((float(row[4]) - float(row[1])) / float(row[1])) * 100
        file_data.append(row)


    # for i in file_data:
    #     print(i)

with open('../Data/GSPC1.csv','w') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter = ',')
    csv_writer.writerows(file_data)

csv_file.close()