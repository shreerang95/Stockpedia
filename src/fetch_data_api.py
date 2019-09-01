import requests
import json

import csv

ctr=1
file=open( "companies2.CSV", "r")
reader = csv.reader(file)
for line in reader:
    company_name = line[0]
    for i in range(1,1000):
        url = 'https://api.intrinio.com/news?identifier='+company_name +'&start_date=2016-01-01&end_date=2018-01-01&page_number='+str(i)
        r = requests.get(url,auth=('9782c8a641b88cb38a5e3fefceaf1336','fd8008d9f7b292bff82df1d368515de7'))
        if(len(r.json()['data'])==0):
            print("Empty @ "+str(i)+" for "+company_name)
            break
        else:
            with open(str(ctr)+'.json','a') as f:
                json.dump(r.json(),f)
                ctr=ctr+1                     