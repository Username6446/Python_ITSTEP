
# day = int(input("Enter number day :: "))

# if day==1:
#     print("Monday")
# elif day==2:
#     print("Tuesday")
# elif day==3:
#     print("Wednsday")
# elif day==3:
#     print("Wednsday")
# elif day==3:
#     print("Wednsday")
# elif day==3:
#     print("Wednsday")
# elif day==3:
#     print("Wednsday")
# else:
#     print("Invalid value")

# match day: #day ==                Switch case
#     case 1:
#         print("Monday")
#     case 2:
#         print("Tuesday")
#     case 3:
#         print("Wednsday")
#     case _:
#         print("Invalid value")

# day = int(input("Enter number day :: "))
# mounth = int(input("Enter number mounth :: "))
# year = int(input("Enter number year :: "))

# print(f"{'0' if day<10 else ''}{day}, {'0' if mounth<10 else ''}{mounth}, {year}")
# days_of_mounth = 0

# match mounth:
#     case 1 | 3 | 5 | 7 | 8 | 10 |12:
#         days_of_mounth = 31
#     case 2:
#         days_of_mounth = 29 if year%4 !=0 and year % 100 !=0 or year%400==0 else 28
#     case 4 | 6 | 9 | 11:
#         days_of_mounth = 30


# day += 1
# if day > days_of_mounth:
#     day = 1
#     mounth+=1

# if mounth > 12:
#     year+=1
#     mounth=1

# print(f"{'0' if day<10 else ''}{day}, {'0' if mounth<10 else ''}{mounth}, {year}")


# тернарний оператор 
# days_of_mounth = 29 if year%4 !=0 and year % 100 !=0 or year%400==0 else 28






# Завдання 1

age = int(input("Enter age : "))
if age>=0 and age<=11:
    print("дитина")
elif age>=12 and age<=18:
    print("підліток")
elif age>=10 and age<=60:
    print("дорослий")
elif age>=61 and age<=150:
    print("пенсіонер")
else:
    print("Print correct age")

# Завдання 2

num = int(input("Enter num : "))
if (num//100)==(num%10) or (num%10)==(num//10%10):
    print("Number have the same digits")
else:
    print("Number have't the same digits")

# Завдання 3

year = int(input("Enter year : "))
if (year%4 ==0 and year % 100 !=0) or year%400==0:
    print("This year is leap")
else:
    print("This year is not leap")

# Завдання 4

number = int(input("Enter number : "))
a = number//10000
b = number//1000%10
# c = number//100%10
d = number%100//10
e = number%10
if a==e and b==d:
    print("Number is a palindrome")
else:
    print("Number is not a palindrome")

# Завдання 5

length = int(input("Enter length : "))
perimetr = int(input("Enter perimetr : "))

diametr = length/(2*3.14)
if (perimetr/4) > diametr:
    print("Yes it can")
else:
    print("No it can't")

# Завдання 6

res = 0
answer1 = int(input('''
Question 1. How many mounth in a year? 
Answer:'''))

if answer1 == 12:
    res+=2

answer2 = int(input('''
Question 2. How many finger on one hand? 
Answer:'''))

if answer2 == 5:
    res+=2

answer3 = int(input('''
Question 3. How many eyes have one human? 
Answer:'''))

if answer3 == 2:
    res+=2

print(res)

# Завдання 7

second = int(input("Enter second : "))
minutes = int(input("Enter minutes : "))
hour = int(input("Enter hour : "))

if second >= 0 and second<60:
    print("Correct seconds")
else:
    print("Incorrect seconds")

if minutes >= 0 and minutes<60:
    print("Correct minutes")
else:
    print("Incorrect minutes")

if hour >= 0 and hour<24:
    print("Correct hour")
else:
    print("Incorrect hour")

# Завдання 8

x = int(input("Enter x : "))
y = int(input("Enter y : "))

if x==0 and y==0:
    print("Dot in the middle")
elif x==0:
    print("Dot on coordinate axis")
elif y==0:
    print("Dot on abscissa axis")
elif x>=0 and y>=0:
    print("I quarter")
elif x<=0 and y>=0:
    print("II quarter")
elif x<=0 and y<=0:
    print("III quarter")
elif x>=0 and y<=0:
    print("IV quarter")


# Завдання 9

mounth = int(input("Enter mounth : "))

match mounth:
    case 1:
        print("January")
    case 2:
        print("February")
    case 3:
        print("March")
    case 4:
        print("April")
    case 5:
        print("May")
    case 6:
        print("June")
    case 7:
        print("July")
    case 8:
        print("August")
    case 9:
        print("September")
    case 10:
        print("October")
    case 11:
        print("November")
    case 12:
        print("December")

