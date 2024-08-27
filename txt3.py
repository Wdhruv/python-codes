count=0
file=open("file/STORY.txt",'r')
line = file.read()
word = line.split()
for w in word:
 if w =='AND':
   count=count+1
print(count)
file.close() 