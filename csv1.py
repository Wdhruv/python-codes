import csv 
f=open("file/data.csv",'r')
d=csv.reader(f)
k=0
adm=int(input("enter admission number"))
next(f)
for row in d:
    if int(row[0])==adm:
        print("adm no =", row[0])
        print("name =", row[1])
        print("class =", row[2])
        print("section =", row[3])
        print("marks =", row[4])
        break
    else:
        print ("records not found")
f.close()