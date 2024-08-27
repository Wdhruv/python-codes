a=input("enter a string: ")
d={}
for i in a:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
for b in d:
    print(b,':',d[b])