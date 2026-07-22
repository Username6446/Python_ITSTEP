
# # Завдання 1
def pr():
    print("\"Don't compare yourself with anyone in this world…\n\tif you do so, you are insulting yourself.\"\n\t\tBill Gates")
pr()

# # # Завдання 2

def func1(a,b):
    for i in range(a,b+1):
        if i%2==0:
            print(i)

a = int(input("Enter num : "))
b = int(input("Enter num : "))
func1(a,b)

# # # # # Завдання 3

def func2(l,d,s):
    if d=="full":
        for i in range(l):
            for j in range(l):
                print(s, end="")
            print()
    elif d=="empty":
        for i in range(l):
            for j in range(l):
                if (j==0 or j==l-1) or (i==0 or i==l-1):
                    print(s, end="")
                else:
                    print(" ", end="")
            print()
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
e = int(input("Enter num : "))

def func3(a,b,c,d,e):
    if a<b and a<c and a<d and a<e:
        return a
    elif b<a and b<c and b<d and b<e:
        return b
    elif c<a and c<b and c<d and c<e:
        return c
    elif d<a and d<b and d<c and b<e:
        return d
    elif e<a and e<c and e<d and e<b:
        return e
    

print(func3(a,b,c,d,e))

# # # # Завдання 5

def func4(num):
    return len(str(num))

num = int(input("Enter num : "))
print(func4(num))

# # # # # Завдання 6

def func5(num):
    rev = 0
    n = num
    while n > 0:
        rev = rev*10+n%10
        n = n//10
    return num==rev

num = int(input("Enter num : "))
print(func5(num))