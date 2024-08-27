s = open("file/Quotes.txt","r")
f = s.read()
z = f.split ()
count = 0
for i in z:
  count = count + 1
  print ("Total number of words:", count)
