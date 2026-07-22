# Завдання 1

a = int(input("Enter num1 :: "))
b = int(input("Enter num2 :: "))

pair = 0
nonpair = 0
nine = 0

for i in range(a,b+1):
    if(i%2==0):
        if(i%9==0):
            nine+=1
        pair+=1
    elif(i%2==1):
        if(i%9==0):
            nine+=1
        nonpair+=1

print(f"Num of pair = {pair}, of nonpair = {nonpair}, nine = {nine}")

# # Завдання 2

num = int(input("Enter num :: "))
char = input("Enter char :: ")

for i in range(num):
    print(char)


# Завдання 3

while True:
    num = int(input("Enter num :: "))
    if num==7:
        print("Good bye")
        break
    elif num>0:
        print("Number is positive")
    elif num<0:
        print("Number is negative")
    elif num==0:
        print("Number is equal to zero")


# Завдання 4
sum=0
max=0
min=100

while True:
    num = int(input("Enter num :: "))
    if num==7:
        print("Good bye!")
        break 
    sum+=num
    if(num>max):
        max=num
    if(num<min):
        min=num
    print(f"Sum = {sum}, max = {max}, min = {min}")


# # Завдання 5

number = int(input("Enter number :: "))
if(number<=1):
    print("Число має бути більшим за 1")

else:
    counter = 0

    for i in range(2, number):
        if(number%i==0):
            counter+=1
        

    print("Proste" if counter==0 else "Skladne")


# Завдання 6
number = int(input("Enter number :: "))
a = 0
b = 1
flag = False
for i in range(10):
    # a,b,c=b,c,a+b
    a,b=b,a+b
    if(number==a):
        flag = True
        break

print(f"Число {number} належить послідовності Фібоначчі" if flag else f"Число {number} не належить послідовності Фібоначчі")
