import csv 
f=open("file/product.csv", "r")
d=csv.reader(f)
print("product whose price more than 300")
print()
for i in d:
    if int(i[2])>300:
        print("product id =",i[0])
        print("product name =",i[1])
        print("product price =",i[2])
        print("--------------------")
f.close()
