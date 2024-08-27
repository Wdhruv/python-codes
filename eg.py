n = input("Enter a Word ")
x =()
for i in range(len(n)):
    if n[i] not in x:
        x.append(n[i])
    else:
        pass
for i in range(len(x)):
    print(x[i], end=" ")