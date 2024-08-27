import csv
f=open("file/data2.csv",'r')
d=csv.reader(f)
r=0
for row in d:
    r=r+1
print("number of records are" ,r)