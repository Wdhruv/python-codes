c = 0
f = open("file/Sample.txt")
line = f.read()
word = line.split()
for w in word:
 if len(w) == 5:
  c += 1
print(c)
