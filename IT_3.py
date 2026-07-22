# # Завдання 1

# tempeture = int(input("Enter tempeture in Celsia :"))
# print(f"Tempeture in Farengeit :{tempeture*9/5+32}")

# # # Завдання 2

# euro = int(input("Enter euro: "))
# rate = float(input("Enter euro rate:"))
# print(f"Dollars: {euro*rate}")

# # # Завдання 3

# num =  int(input("Enter number:"))
# print(f"{num%10}/n{num//10}")

# # Завдання 4

# num1 = input("Enter number1 :")
# num2 = input("Enter number2 :")
# print(num1+""+num2)

# # # Завдання 5

# number = int(input("Enter number -> "))
# third = number%10
# second = number//10%10
# first = number//100
# print(f"{first}\n{second}\n{third}\n{first+second+third}")


# # # Завдання 6

# money = int(input("Enter money :"))
# percent = int(input("Enter percent :"))

# money+= money / 100 * percent
# print(f"Year 1 ==> {money}")

# money+= money / 100 * percent
# print(f"Year 2 ==> {money}")

# money+= money / 100 * percent
# print(f"Year 3 ==> {money}")

# money+= money / 100 * percent
# print(f"Year 4 ==> {money}")

# money+= money / 100 * percent
# print(f"Year 5 ==> {money}")


# Рівень 2 



# # # # Завдання 6
# print("\n\n\n\n\n\n\n\n\n\n")
# print(chr(9556),chr(9552)*50,chr(9559), sep="")
# print("\n")
# print(chr(9553)," "*10,"Pory Roku", " "*27,chr(9553))
# print("\n")
# print(chr(9568),chr(9552)*10,chr(9574),chr(9552)*11,chr(9574),chr(9552)*11,chr(9574),chr(9552)*15,chr(9571), sep="")
# print("\n")
# print(chr(9553)," " ,"Zyma", " " ,chr(9553)," " ,"Vesna", " ",chr(9553)," " ,"Lito", "  ",chr(9553)," " ,"Osin", "      ",chr(9553),)
# print("\n")
# print(chr(9562),chr(9552)*50,chr(9565), sep="")


# # # # Завдання 7

# cost = int(input("Enter cost: "))
# num_of_laptops = int(input("Enter munber of laptops: "))
# sale = int(input("Enter sale: "))
# print(f"Sum = {cost*num_of_laptops-cost*num_of_laptops*sale/100}")

# # # # Завдання 8

# sum_of_agreement = int(input("Enter num of agreement: "))
# print(f"Wage = {100+sum_of_agreement*5/100}$")

# # # # Завдання 9

# size = int(input("Enter size: "))
# speed = int(input("Enter speed in b/sec: "))

# size = size * 8_589_934_592
# time = size/speed
# hours = time//3600
# minutes = (time-hours*3600)//60
# seconds = time - (time-hours*3600) - (time-hours*3600)//60

# print(f"Hours = {hours}, minutes = {minutes} seconds = {seconds}")


# # # # Завдання 10

# hours1 = int(input("Enter hours1: "))
# minuts1 = int(input("Enter minuts1: "))
# seconds1 = int(input("Enter seconds1: "))

# hours2 = int(input("Enter hours2: "))
# minuts2 = int(input("Enter minuts2: "))
# seconds2 = int(input("Enter seconds2: "))


# h = hours2-hours1
# m = h*60+minuts2-minuts1
# s = m*60+seconds2-seconds1//60
# print(f"Sum = {(s*2)}grn")

# # # # Завдання 11

length = int(input("Enter lenSgth: "))
cost_100 = int(input("Enter cost_100: "))
cost_1 = int(input("Enter cost_1: "))
cost_2 = int(input("Enter cost_2: "))
cost_3 = int(input("Enter cost_3: "))

print("\n\n\n\n\n\n\n\n\n\n")
print(chr(9556),chr(9552)*10,chr(9574),chr(9552)*10,chr(9574),chr(9552)*10,chr(9559), sep="")
print(chr(9553)," cost_1 ",chr(9553)," cost_2 ",chr(9553)," cost_3 ",chr(9553))
print(chr(9568),chr(9552)*10,chr(9580),chr(9552)*10,chr(9580),chr(9552)*10,chr(9570), sep="")
print(f"{chr(9553)}    {cost_1*cost_100*length}     {chr(9553)}     {cost_2*cost_100*length}    {chr(9553)}    {cost_3*cost_100*length}     {chr(9553)}")
print(chr(9562),chr(9552)*10,chr(9577),chr(9552)*10,chr(9577),chr(9552)*10,chr(9565), sep="")


