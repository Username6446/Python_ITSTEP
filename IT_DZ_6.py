# Завдання 1

num1=int(input("Enter num1 : "))
num2=int(input("Enter num2 : "))

while num1<num2:
    if(num1%7==0):
        print(num1)
    num1+=1
# Завдання 2

n1=int(input("Enter num1 : "))
n2=int(input("Enter num2 : "))
temp1=n1
temp2=n2
while temp1<=n2:
    print(temp1)
    temp1+=1
print("")
while temp2>=n1:
    print(temp2)
    temp2-=1
print("")
temp1=n1
while temp1<n2:
    if(temp1%7==0):
        print(temp1)
    temp1+=1
print("")
temp1=n1
count=0
while temp1<n2:
    if(temp1%5==0):
        count+=1
    temp1+=1
print(count)
# Завдання 3

a1 = int(input("Enter num1 : "))
a2 = int(input("Enter num2 : "))

while a1<a2:
    if(a1%3==0 and a1%5==0):
        print("Fizz Buzz")
    elif(a1%3==0):
        print("Fizz")
    elif(a1%5==0):
        print("Buzz")
    a1+=1

# Завдання 4

num1 = int(input("Enter num1 : "))
num2 = int(input("Enter num2 : "))
leap = int(input("Enter leap : "))
choice = int(input("Choose descent 0 = up, 1 = down : "))

if choice==0:
    while num1<num2:
        print(num1)
        num1+=leap
elif choice==1:
    while num2>num1:
        print(num2)
        num2-=leap
else:
    print("Inccorect input")

# Завдання 5

num1 = int(input("Enter num1 : "))
num2 = int(input("Enter num2 : "))

if(num1>num2):
    temp=num2
    num2=num1
    num1=temp
n=0
while num1<num2:
    if(num1%4==0 and num1%6!=0):
        print(num1)
        n+=1
    num1+=1
if(n==0):
    print("No numbers")

# Завдання 6

num1 = int(input("Enter num1 : "))
num2 = int(input("Enter num2 : "))
sum=1
temp = num1
while sum<num2:
    num1*=temp
    sum+=1
print(num1)