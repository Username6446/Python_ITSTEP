

a = 6
b = 7

'''
<
>
<=
>=


'''

# print(f"{a} > {b} --> {(a > b)}")
# print(f"{a} < {b} --> {(a < b)}")
# print(f"{a} >= {b} --> {(a >= b)}")
# print(f"{a} <= {b} --> {(a <= b)}")
# print(f"{a} == {b} --> {(a == b)}")
# print(f"{a} != {b} --> {(a != b)}")

login = "mka"

# print(f"login = 'mka'  --> {(login == 'mka')}")
# print(f"login = 'Mka'  --> {(login == 'Mka')}")

# and, or

password = "mka5"

# print(login == 'mka' and password == 'mka')
# print(login == 'mka' and password == 'mka5')

# month = int(input("Enter month --> "))
# print(month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12)

# print(1 + False)

# year = int(input("Enter year --> "))
# print(((year%4==0) and (year%100!=0)) or (year%400==0) + 365)

# if login == 'mka' and password == 'mka5':
#     print("Welcome")
# else:
#     print("Error")

# day = int(input("Enter number day : "))
# if day == 1 :
#     print("Monday")
# elif day == 2:
#     print("Tuesday")
# elif day == 3:
#     print("Wednsday")
# elif day == 4:
#     print("Thursday")
# elif day == 5:
#     print("Friday")
# elif day == 6:
#     print("Saturday")
# elif day == 7:
#     print("Sunday")
# else:
#     print("Error")
# print("="*100)

# number = int(input("Enter number :"))
# if number>=0 and number<=20:
#     print("number is in range")
# elif number<0 or number>20:
#     print("number is not in range")
# else:
#     print("Error")

# login = input("Enter login : ")
# if login == "cancel":
#     print("login canceled")
# elif login == "admin":
#     passwoed = input("Enter password :")
#     if passwoed == "step":
#         print("Welcome")
#     elif passwoed == "canceled":
#         print("login canceled")
#     else:
#         print("Error password")
# else:
#     print("I don't know you")


# # Завдання 1
# number = int(input("Enter number : "))
# if number%2==0:
#     print(f"{number} Even number")
# else:
#     print(f"{number} Odd number")

# # Завдання 2
# num = int(input("Enter num : "))
# if num%7==0:
#     print(f"{num} Number is multiple 7")
# else:
#     print(f"{num} Number is not multiple 7")


# # Завдання 3

# a = int(input("Enter a : "))
# b = int(input("Enter b : "))
# if a>b:
#     print(a)
# else:
#     print(b)

# Завдання 4

# a = int(input("Enter a : "))
# b = int(input("Enter b : "))
# if a<b:
#     print(a)
# else:
#     print(b)

# # Завдання 5

# num1 = int(input("Enter num1 : "))
# num2 = int(input("Enter num2 : "))
# operator = str(input("Enter operator :"))

# if operator=='+':
#     print(int(num1+num2))
# elif operator=='-':
#     print(int(num1-num2))
# elif operator=="Average":
#     print(int((num1+num2)/2))
# elif operator=='*':
#     print(int(num1*num2)) 
# else:
#     print("Enter correct oparator")

# # Завдання 5

# sum = int(input("Enter sum : "))
# op = str(input("Enter EUR, GBP, JPY : "))

# if op=='EUR':
#     rate = float(input("Enter EUR rate : "))
#     print(f"{sum*rate}")
# elif op=='GBP':
#     rate = float(input("Enter GBP rate : "))
#     print(f"{sum*rate}")
# elif op=='JPY':
#     rate = float(input("Enter JPY rate : "))
#     print(f"{sum*rate}")
# else :
#     print("Enter correct value") 

choice = int(input('''
               
    Select operation 
               1-sum
               2-sub
               3-mult
               4-div
        
               Enter --> '''))
a=5
b=7

if choice==1:
    print(a+b)
else:
    print("Error")