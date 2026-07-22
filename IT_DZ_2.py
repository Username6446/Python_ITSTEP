# Завдання 1

one = int(input("Enter number1 ::"))
two = int(input("Enter number2 :: "))
three = int(input("Enter number3 :: "))
print(f"{one} + {two} + {three} = {one + two + three}")
print(f"{one} * {two} * {three} = {one * two * three}")

# Завдання 2

diagonal_1 = int(input("Enter diagonal_1 ::"))
diagonal_2 = int(input("Enter diagonal_2 :: "))
print(f"Area of rhombus = {float(diagonal_1*diagonal_2/2)}")

# Завдання 3

wage = float(input("Enter wage ::"))
credit = float(input("Enter credit ::"))
debt = float(input("Enter debt ::"))
print(f" {float(wage-credit-debt)} grn left")

# Завдання 4

distance = int(input("Enter wage ::"))
cost = float(input("Enter cost ::"))
litrs = float(input("Enter litrs ::"))
print(f"Cost of the trip = {float(distance*litrs/100*cost)} grn")

# Завдання 5

sum = int(input("Enter sum :"))
people = int(input("Enter num of people :"))
tips = sum*15/100
sum = sum + tips

print(f"Every person has to pay = {float(sum/people)} grn")

# Завдання 6

day_cost = float(input("Enter day_cost :"))
days = int(input("Enter num of days :"))
pledge = float(input("Enter num of days :"))

rental_cost = day_cost*days

print(f"Need to pay with pledge= {float(rental_cost+pledge)} grn")
print(f"Need to pay (pledge returned)= {float(rental_cost)} grn")
print(f"Need to pay for a day = {float(rental_cost/days)} grn")
