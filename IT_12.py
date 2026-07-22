import re

def printMessage(name = "None", last_name = "fdsg"):
    print(f"Hello \n First name : {name} \n Last name : {last_name}") 

printMessage("Masha", "Bondar")
printMessage("Pasha")
printMessage(last_name="Sasha")
printMessage()


def summ(a,b):
    return a + b
def sub(a,b):
    return a - b
def mult(a,b):
    return a * b
def div(a,b):
    if b==0:
        print("Error! Division by zero!")
    else:
        return a / b

def calculate(a,b, op):
    match op:
        case '+':
            return summ(a,b)
        case '-':
            return sub(a,b)
        case '*':
            return mult(a,b)
        case '/':
            return div(a,b)
    print("error operation")

def findOperation(input):
    match = re.search('[+-\/\*]',input)
    return match[0] if match else None

def printRes(input):
    if len(input) < 3:
        print("Error!!!")
        return
    elif len(input.split()) == 3:
        input = input.split()
        op = input[1]
        numb_2 = int(input[2])
    else:
        match = findOperation(input)
        if match:
            input = input.split(match)
            op = match 
            numb_2 = int(input[1])
        else:
            return
    numb_1 = int(input[0])
       
    print(f"{numb_1} {op} {numb_2} = {calculate(numb_1,numb_2,op)}")
numb_1 = 5
numb_2 = 7

# print(f"{numb_1} + {numb_2} = {summ(numb_1, numb_2)}")
# print(f"{numb_1} - {numb_2} = {sub(numb_1, numb_2)}")
# print(f"{numb_1} * {numb_2} = {mult(numb_1, numb_2)}")
# print(f"{numb_1} / {numb_2} = {round(div(numb_1, numb_2),2)}")

# ex = input("Enter :: ") # 2 + 2

# numb_1 = int(ex[0])
# numb_2 = int(ex[2])
# print(f"{numb_1} {ex[1]} {numb_2} = {calculate(numb_1,numb_2,ex[1])}")

# printRes(ex)
# findOperation(ex)

# def sum_all(*numbers):
#     sum = 0
#     for i in numbers:
#         sum+=i
#     return sum

# def printMatrix(mat):
#     for row in mat:
#         for item in row:
#             print(item, end="\t")
#         print()
# print(sum_all(3,4,5,6))

# import random
# matrix = [[random.randint(1,20) for i in range(4)] for j in range(4)]
# printMatrix(matrix)




# # Завдання 1
def pr():
    print("Don't let the noise of others' opinions\n\tdrown out your own inner voice.\"\n\t\t Steve Jobs")
pr()

# # # Завдання 2

def func1(a,b):
    for i in range(a,b+1):
        if i%2==1:
            print(i)

a = int(input("Enter num : "))
b = int(input("Enter num : "))
func1(a,b)

# # # # Завдання 3

def func2(l,d,s):
    if d=="horiz":
        for i in range(l):
            print(s)
    elif d=="vertic":
        for i in range(l):
            print(s,end="")
    else:
        print("Error!")

length = int(input("Enter length : "))
direction = input("Enter direction : ")
symb = input("Enter symb : ")

func2(length,direction,symb)

# # # # Завдання 4

a = int(input("Enter num : "))
b = int(input("Enter num : "))
c = int(input("Enter num : "))
d = int(input("Enter num : "))

def func3(a,b,c,d):
    if a>b and a>c and a>d:
        return a
    elif b>a and b>c and b>d:
        return b
    if c>b and c>a and c>d:
        return c
    elif d>a and d>c and d>b:
        return d

print(func3(a,b,c,d))
# # # Завдання 5

def func4(num):
    for i in range(2,(num//2)):
        if num%i==0:
            return False
    return True

num = int(input("Enter num : "))
print(func4(num))

# # # # Завдання 6

def func5(num):
    n1 = num//100000
    n2 = num//10000%10
    n3 = num//1000%100%10
    n4 = num%1000//100
    n5 = num%1000//10%10
    n6 = num%10000%10
    if n1+n2+n3==n4+n5+n6:
        return True
    else:
        return False

num = int(input("Enter num : "))
print(func5(num))