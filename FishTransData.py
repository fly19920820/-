# -*- coding: big5 -*-
import urllib2
import datetime
import json
import csv

request = urllib2.Request("http://m.coa.gov.tw/OpenData/AquaticTransData.aspx")
response = urllib2.urlopen(request)
html = response.read()

jsonData = json.loads(html)

csvData = []


for item in jsonData:
    titleList = []
    for key in item.keys():
        titleList.append(key.encode('big5'))
    csvData.append(titleList)
    break
    

for item in jsonData:
    rowList = []
    for value in item.values():
        try:
            rowList.append(value.encode('big5'))
        except:
            rowList.append(value.encode('utf8'))
    csvData.append(rowList)
    
current = datetime.datetime.now().strftime("%Y-%m-%d")
fileName = "FishTransDataSet/"+current+".json"
csvFileName = "FishTransDataSet/"+current+".csv"

#fileout = file(fileName,"w")
#fileout.write(html)
#fileout.close()

fileout = open(csvFileName,"wb")  
w = csv.writer(fileout)  
w.writerows(csvData)  
fileout.close() 
