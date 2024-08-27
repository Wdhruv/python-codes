import csv
field=["roll no" , "name" , "class"]
f=open("file/data1.csv",'w')
d=csv.writer(f)
d.writerow(field)
ch='y'
while ch=='y' or ch=='Y':
    rn=int(input("enter roll number: "))
    nm=input("enter name:")
    cls=input("enter class: ")
    rec=[rn,nm,cls]
    d.writerow(rec)
    ch==input("enter more records??(Y/N)")
    if ch!="Y":
        break
f.close()
