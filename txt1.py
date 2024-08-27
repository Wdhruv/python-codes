f=open("file/Country.txt",'r')
W,H=0,0
r=f.read()
for x in r:
 if x[0]=="W" or x[0]=="w":
  W=W+1
 elif x[0]=="H" or x[0]=="h":
  H=H+1
f.close()
print("W or w :", W)
print("H or h :", H)