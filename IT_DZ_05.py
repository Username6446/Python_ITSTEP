# Завдання 1

day = int(input("Enter day : "))

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednsday")
    case 4:
        print("Thusday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sanday")
    case _:
        print("Incorrect input")

# Завдання 2

mounth = int(input("Enter mounth : "))

match mounth:
    case 1:
        print("січень")
    case 2:
        print("лютий")
    case 3:
        print("березень")
    case 4:
        print("квітень")
    case 5:
        print("травень")
    case 6:
        print("червень")
    case 7:
        print("липень")
    case 8:
        print("серпень")
    case 9:
        print("вересень")
    case 10:
        print("жовтень")
    case 11:
        print("листопад")
    case 12:
        print("грудень")

# Завдання 3

sum = int(input("Enter sum : "))
age = int(input("Enter age : "))
percent = 0
if age>=0 and age<=18:
    percent = 10
elif age>=18 and age<=60:
    percent=5
elif age>=60 and age<=150:
    percent = 15
else:
    print("Inccorect input")

print(f"Sum = {sum-sum*percent/100}")

# Завдання 4

num1 = int(input("Enter mark1: "))
num2 = int(input("Enter mark2: "))
num3 = int(input("Enter mark3: "))

if (num1>0 and num1<=5) and (num2>0 and num2<=5) and (num3>0 and num3<=5):
    print("")
else:
    print("Inccorect input")

if num1==2 or num2==2 or num3==2:
    print("Незадовільно")
elif num2>3 or num2>3 or num3>3:
    print("Відмінно")

# Завдання 5

n1 = int(input("Enter mark1: "))
n2 = int(input("Enter mark2: "))
n3 = int(input("Enter mark3: "))
n4 = int(input("Enter mark4: "))


if (n1>0 and n1<=5) and (n2>0 and n2<=5) and (n3>0 and n3<=5) and (n4>0 and n4<=5):
    print("")
else:
    print("Inccorect input")

if n1<3 or n2<3 or n3<3:
    print("студент не допускається до іспиту")
elif n1>3 and n2>3 and n3>3:
    print("студент допускається до іспиту з відзнакою")
else:
    print("студент допускається до іспиту")

# Завдання 6

car_age = int(input("Enter age of car : "))
car_mileage = int(input("Enter car_mileage (km): "))

if car_age<3 and car_mileage<30000:
    print("Автомобіль у відмінному стані")
elif car_age<10 and car_mileage<100000:
    print("Автомобіль у хорошому стані")
else:
    print("Автомобіль потребує перевірки")