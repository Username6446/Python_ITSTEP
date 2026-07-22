# Завдання 1

num1 = int(input("Enter number 1 : "))
num2 = int(input("Enter number 2 : "))
num3 = int(input("Enter number 3 : "))
operator = input("Enter + or * : ")

if operator=="+":
    print(num1+num2+num3)
elif operator=="*":
    print(num1*num2*num3)
else:
    print("Enter correct operator")

# Завдання 2

num_1 = int(input("Enter number 1 : "))
num_2 = int(input("Enter number 2 : "))
num_3 = int(input("Enter number 3 : "))
operator_2 = input("Enter min, max, or average : ")

if operator_2=="min":
    if num_1<num_2 and num_1<num_3:
        print(f"Min is {num_1}")
    elif num_2<num_1 and num_2<num_3:
        print(f"Min is {num_2}")
    elif num_3<num_1 and num_3<num_2:
        print(f"Min: {num_3}")
    else:
        print("No Min number")
elif operator_2=="max":
    if num_1>num_2 and num_1>num_3:
        print(f"Max is {num_1}")
    elif num_2>num_1 and num_2>num_3:
        print(f"Max is {num_2}")
    elif num_3>num_1 and num_3>num_2:
        print(f"Max: {num_3}")
    else:
        print("No Max number")
elif operator_2=="average":
    print(f"Average: {(num_1+num_2+num_3)/3}")
else:
    print("Enter correct operator")

# # Завдання 3

num = int(input("Enter num: "))
if num==1:
    print("Дуже погано")
elif num==2:
    print("Погано.")
elif num==3:
    print("Задовільно.")
elif num==4:
    print("Добре.")
elif num==5:
    print("Відмінно.")
else:
    print("Enter number from 1 to 5")

# Завдання 4

metrs = int(input("Enter metrs : "))
choice = int(input('''
               
    Вибери один з варіантів:
                    
            1. Перевести або в милі або в дюйми або в ярди.
            2. Перевести в милі, дюйми та ярди
            3. Перевести в кілометри та сантиметри
               Ввід --> '''))

if choice==1:
    str = input("Enter miles, inches or yards : ")
    if(str=="miles"):
        print(metrs*39.37)
    elif (str=="inches"):
        print(metrs*1.09)
    elif (str=="yards"):
        print(metrs*0.00062)
    else:
        print("Enter correct choice")
elif choice==2:
    print(f"Miles: {metrs*39.37}, Inches: {metrs*1.09}, Yards: {metrs*0.00062}")
elif choice==3:
    print(f"Kilometrs: {metrs/1000}, Santimetrs: {metrs*100}")
else:
    print("Enter correct choice")

# Завдання 5

num11 = int(input("Enter num1 : "))
num22 = int(input("Enter num2 : "))
operator1 = str(input("Enter operator :"))

if operator1=='+':
    print(int(num11+num22))
elif operator1=='-':
    print(int(num11-num22))
elif operator1=='*':
    print(int(num11*num22)) 
elif operator1=='/':
    print(int(num11/num22)) 
elif operator1=='%':
    print(int(num11%num22)) 
elif operator1=='**':
    print(int(num11**num22)) 
else:
    print("Enter correct oparator")


# Завдання 6

number = int(input("Enter number : "))

if number<100 or number>999:
    print("Enter number with 3 digit:")
    number = int(input("Enter number : "))
    

if((number%10)==(number//100) and (number//100)==(number//10%10)):
    print("Всі цифри однакові")
else:
    print("Цифри різні")


#Зробити перевірку чи це 3-х значне число
