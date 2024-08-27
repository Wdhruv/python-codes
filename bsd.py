print("Half Pyramid Pattern of Alphabets: ")
val = 65
for i in range(5):
    for j in range(i+1):
        ch = chr(val)
        print(ch, end=" ")
    val = val+1
    print()