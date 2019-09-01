# script to find top 3 and bottom 3 companies for each day

import csv
import json
import datetime as dt

#finding top 3 and bottom 3 script

data=[]

# with open("../Data/all_stocks_5yr_pchange.csv") as csvf:
#     file = csv.reader(csvf,delimiter=",")
#     for row in file:
#         data.append(row)
#
# for i in range(1,len(data)):
#     # pchange=0
#     # print(i)
#     pchange = ((float(data[i][4]) - float(data[i][1]))/float(data[i][1])) * 100
#     data[i].append(pchange)

# print(data)

# with open("../Data/all_stocks_5yr_pchange1.csv",mode='w') as csvf1:
#     fwriter = csv.writer(csvf1,delimiter=",",lineterminator='\n')
#     for i in data:
#         fwriter.writerow(i)


# with open("../Data/all_stocks_5yr_pchange1.csv") as csvf:
#     file = csv.reader(csvf,delimiter=",")
#     for row in file:
#         data.append(row)
#
# mydict={}
# mydict1={}
# d = data[1][0]
# l = []
# j = 1
# while (data[j][0] == d):
#     l.append(data[j])
#     j = j + 1
# l2 = []
# l2.append(l[:3])
# l2.append(l[-3:])
# for k in l2[0]:
#     mydict1[k[6]] = k[7]
# for k in l2[1]:
#     mydict1[k[6]] = k[7]
#
# mydict[d] = mydict1
#
# print(mydict)

# i=1
# while(i<len(data)):
#     mydict1={}
#     d = data[i][0]
#     l = []
#     j = i
#     flag=0
#     while(flag==0 and j<len(data)):
#         if(data[j][0] == d):
#             # print(j)
#             l.append(data[j])
#             j = j + 1
#         else:
#             flag=1
#
#     # print(j)
#     l2 = []
#     l2.append(l[:3])
#     l2.append(l[-3:])
#     for k in l2[0]:
#         mydict1[k[6]] = k[7]
#     for k in l2[1]:
#         mydict1[k[6]] = k[7]
#
#     mydict[d] = mydict1
#     i = j

# print(mydict)


# with open("../Data/top_bottom_companies.json",mode='w') as jsonf:
#     json.dump(mydict,jsonf)




# my_dict = {}
# with open('../Data/top_bottom_companies.json', 'r') as fp:
#     my_dict = json.load(fp)
#
# # print(my_dict)
#
# newjson={}
#
# for i in my_dict.keys():
# 	t = dt.datetime.strptime(i,"%d-%m-%y")
# 	t1 = t.strftime("%Y-%m-%d")
# 	# print(t1)
# 	newjson[t1] = my_dict[i]
#
# print(newjson)
#
# with open('../Data/top_bottom_companies1.json', 'w') as fp:
#     json.dump(newjson, fp)