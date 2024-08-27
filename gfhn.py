a1 = int(input("Enter first number: "))
b2 = int(input("Enter second number: "))
min_num = min(a1,b2)
hcf = 1
for i in range(1, min_num + 1):
    if a1 % i == 0 and b2 % i == 0:
        hcf = i
print("HCF of", a1, "and", b2, "is", hcf)