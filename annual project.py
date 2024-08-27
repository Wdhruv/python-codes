import time
import random 
OP = ["+", "-", "*"]
mina = 3
maxa = 12
tp = 10
 
def generate_problem():
    left= random.randint(mina, maxa)
    right = random.randint(mina , maxa)
    operator= random.choice(OP)

    expr= str(left) + " " + operator + " " + str(right)
    answer = eval(expr)
    return expr, answer

wrong = 0 
input("press enter to start")
print("--------------------")
 
start_time = time.time()

for i in range(tp):
    expr, answer = generate_problem()
    while True:
        guess = input ("problem #" + str(i + 1) + ": " + expr + " = ")
        if guess == str(answer):
            break
        wrong += 1

end_time = time.time()
total_time = end_time - start_time

print("-----------")
print("gges  you finished in " , total_time, "seconds!")