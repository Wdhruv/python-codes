c=0
a=input("enter a sentence: ")
b=input("enter the alphabet you want to count")
for i in a:
    if i==b:
        c=c+1
print ("the no of ",b,"occuring is",c)