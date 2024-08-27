import csv
f=open("file/student.csv","r")
d=csv.reader(f)
print("student scored more than 80")
print()
for i in d:
    if int(i[2])>80:
        print("roll number=", i[0])
        print("name =", i[1])
        print("marks =", i[2])
        print('----------------')
f.close()
