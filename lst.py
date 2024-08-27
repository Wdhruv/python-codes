a=int(input("enter date :"))
b=int(input("enter month :"))
c=int(input("enter year :"))
days=[31,28,31,30,31,30,31,31,30,31,30,31]
e=int(input("enter the number of days you want to add:"))
a=a+e
while a>days[b-1]:
    a=a-days[b-1]
    b=b+1
    if b>12:
        b=1
        c=c+1
print("the date after",e,"day is:",a,"/",b,"/",c)