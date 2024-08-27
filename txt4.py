count=0
file=open("file/STORY2.txt",'r')
line = file.read()
word = line.split()
for w in word:
 if w[0] =='t' or w[0]=='T':
  count=count+1
  print(count)
file.close()