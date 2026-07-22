# word = "hello"

# for letter in word:
#     print(letter + " - ", end="")
########
# for i in range(10):
#     print(i+1, end="\t")
########

# start = 1
# end = 10
# print()
# for el in range(start, end):
#     print(el, end="\t")
#     print()
    
########

# for i in range(2,21,2):
#     print(i, end="\t")

#########

# range(start, end, step)

#########

# number = int(input("Enter number :: "))
# counter = 0

# for i in range(2, number):
#     if(number%i==0):
#         counter+=1
    

# print("Proste" if counter==0 else "Skladne")

#########

# number = int(input("Enter number :: "))
# flag = True
# for i in range(2, number//2):
#     if(number%i==0):
#         flag=False
#         break

# print("Prime number" if flag else "Complex number")
    
import random

# for i in range(5):
#     rnd = int(random.random()*10)# (1, 10)
#     print(rnd)
    
#     rnd = random.choice("spr")
#     print(rnd, end="\t")

# ###################################################

# U_w = 0
# B_w = 0
# D = 0

# while True:
#     user_score = 0
#     bot_score = 0
#     for i in range(5):
#         print('-'*15 + f"Round #{i+1} " + '-'*15)
#         while True:
#             user = input('''
#                 [r] - rock             
#                 [s] - scissors
#                 [p] - paper
#                 [l] - lizard
#                 [k] - spock
#                     enter choice :: ''')
#             if user == 'r' or user =='p' or user =='s' or user =='l' or user =='k':
#                 break
#             else:
#                 print("\033[31m Error!!! Enter true choice \033[0m ")
        
#         bot = random.choice('rsplk')
#         print(f"\t\t Bot \t User")
#         print(f"\t\t [{bot}] \t [{user}]\n")

#         if((user == 'r' and (bot =='s' or bot == 'l')) or (user == 's' and (bot =='p' or bot == 'l')) or (user =='p' and (bot =='r' or bot == 'k')) or (user =='l' and (bot =='p' or bot == 'k')) or (user =='k' and (bot =='s' or bot == 'r'))):
#             user_score +=1
#         elif user!=bot:
#             bot_score+=1

#     if user_score>bot_score:
#         print('-'*15 + f"Congratilations " + '-'*15)
#         U_w+=1
#     elif bot_score>user_score:
#             print('-'*15 + f"Sorry! You Loser " + '-'*15)
#             B_w+=1
#     else:
#             print('-'*15 + f"Draw " + '-'*15)
#             D+=1
    
#     ch = int(input("Enter 1 if you want to continue game :: "))
#     if ch!=1:
#         print(f"Game is over\nUser won - {U_w}\n Bot won - {B_w}\n Draw - {D}")
#         break

     

# # ################################################### Завдання 1

# a = int(input("Enter num1 :: "))
# b = int(input("Enter num2 :: "))
# sum = 0
# for i in range(a, b+1):
#     sum+=i
# print(f"sum = {sum}, Average = {sum/(b-a+1)}")





# # ## Завдання 2

# num = int(input("Enter num1 :: "))
# fact = 1
# for i in range(2,num+1):
#     fact*=i
# print(f"Factorial = {fact}")



# # ## Завдання 3

# num = int(input("Enter num :: "))
# for i in range(num):
#     print("*",sep="", end="")


# # # ## Завдання 4

# num = int(input("Enter num :: "))
# char = input("Enter char :: ")

# for i in range(num):
#     print(f"{char}",sep="", end="")


# # ## Завдання 5

# while True:
#     i = int(input("Enter num (1 - min) (2 - max) (3 - end) :: "))
#     if(i==3):
#         print("End")
#         break
#     elif(i==1):
#         a = int(input("Enter num1 :: "))
#         b = int(input("Enter num2 :: "))
#         if(a>b):
#             print(f"{b} is min")
#         elif(a<b):
#             print(f"{a} is min")
#         else:
#             print("numbers are equals")
#     elif(i==2):
#         a = int(input("Enter num1 :: "))
#         b = int(input("Enter num2 :: "))
#         if(a>b):
#             print(f"{a} is max")
#         elif(a<b):
#             print(f"{b} is max")
#         else:
#             print("numbers are equals")
#     else:
#         print("inccorect input")




# ## Завдання 6

# while True:
#     i = int(input("Enter num (1 - add) (2 - sub) (3 - div) (4 - end) :: "))
#     if(i==4):
#         print("End")
#         break
#     elif(i==1):
#         a = int(input("Enter num1 :: "))
#         b = int(input("Enter num2 :: "))
#         print(f"{a} + {b} = {a+b}")
#     elif(i==2):
#         a = int(input("Enter num1 :: "))
#         b = int(input("Enter num2 :: "))
#         print(f"{a} - {b} = {a-b}")
#     elif(i==3):
#         a = int(input("Enter num1 :: "))
#         b = int(input("Enter num2 :: "))
#         print(f"{a} / {b} = {a//b}")
#     else:
#         print("inccorect input")

