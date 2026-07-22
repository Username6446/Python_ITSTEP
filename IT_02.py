print("\n\n");

# print(12, type(13)) # number (int)
# print(13.5, type(13.5)) # number (float)
# print("Hello", type("Hello")) # string (str)
# print(True, type(True)) # boolean (bool)


# first_name = "Alex"
# age = 18 #number()
# PI = 3.14
# flag = True

# print(first_name, type(first_name))
# print(age, type(age))
# print(PI, type(PI))
# print(flag, type(flag))



# name = "Ivan"
# number = 5;
# result = name + 5
# print(result)

'''

/
*
+
-
%   - remainder
//  - division with remainder 
**  - pow

priority:

()
//,**,%
/,*
+,-

'''

# one,two = 9,5  # one = 7, two = 5

# result_sum = one + two
# print(one, "+", two, "=", result_sum)
# print("{} + {} = {}".format(one, two, result_sum))

# print(f"{one} + {two} = {one + two}")
# print(f"{one} - {two} = {one - two}")
# print(f"{one} * {two} = {one * two}")
# print(f"{one} / {two} = {one / two}")
# print(f"{one}// {two} = {one // two}")
# print(f"{one} % {two} = {one % two}")
# one,two = 2,4
# print(f"{one} ** {two} = {one ** two}")


# big_number = 1e-5 # 1 * 10^(-5)
# print(big_number)

# number = 13
# flag = True
# result = number + flag
# print(f"Result :: {result} {type(result)}")  

# 13 + 1    1 = True 0 = False
# приводиться до інт бо він може мати більше значень а бул може мати лише 2 значення 

# result = number + 3.14
# print(f"Result :: {result} {type(result)}")

# one = int(input("Enter number :: "))
# two = input("Enter number :: ")
# two = int(two)
# print(f"{one} + {two} = {one+two}") # просто склеїться

# print(one)
# print(two)

# print(int(float("45.5")))
# print(bool(-1))



# # Завдання 1
# one = int(input("Enter number1 ::"))
# two = int(input("Enter number2 :: "))
# print(f"{one} + {two} = {one + two}")
# print(f"{one} - {two} = {one - two}")
# print(f"{one} * {two} = {one * two}")

# # Завдання 2
# number = int(input("Enter number1 ::"))
# percent = int(input("Enter number1 ::"))
# print(f"{percent}% = {number / 100 * percent}")

# # Завдання 3
# width = int(input("Enter width ::"))
# height = int(input("Enter height ::"))
# print(f"Area of rectangle = {width*height}")

# # Завдання 4
# side = int(input("Enter side ::"))
# print(f"Perimetr of sqaure = {side*4}")

# # Завдання 5
# metrs = int(input("Enter metrs ::"))
# print(f"In {metrs} metrs = {metrs*100} santimetrs")

# # Завдання 6
# litrs_of_paints = float(input("Enter litrs_of_paints ::"))
# print(f"To paint 4 sides need {litrs_of_paints*4} santimetrs")





# # Завдання 1

# grn = int(input("Enter grn ::"))
# cop = int(input("Enter cop ::"))
# cop = cop/100*10
# print(f"{grn} грн {int(cop)} коп")

# print("\n\n")

# # Завдання 2
# print("\t Обчислення відстані між населеними пунктами.\n")
# print("\t\t Введіть вихідні дані:\n")

# scale = int(input("\t\t Масштаб карти (кількість кілометрів в одному сантиметрі) ->"))
# length = float(input("\n\t\t Відстань між точками, які зображують населені пункти (см) -> "))
# print(f"\n Відстань між населеними пунктами {scale*length} км.")

# Завдання 4
# money = float(input("Enter money :"))
# print(f"{int(money)} грн {int((money - int(money))*100)} грн")

# # Завдання 5
# days = int(input("Enter days :"))
# print(f"{int(days//7)} тижні {days%7} днів")
