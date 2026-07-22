

# i=1

# while i>1:
#     i-=1
#     print(f"{i} ", end="")
# else:
#     print("=================")
    
# print("=================")

####################
# number = int(input("Enter number : "))

# i=0

# while i<number:
#     print(i, end="\t")
#     i+=1

#####################

# while True:
#     number = int(input("Enter number : "))
#     if number==4:
#         print("Correct answer")
#         break
# print("============")

######################

# i=0
# while i<5:
#     color = input("Enter color : ")
#     i+=1

#     if color == "red":
#         continue
#     elif len(color) == 5:
#         print("2ew")
#     else:
#         print(color)  
######################

# number = int(input("Enter number : "))
# res=0
# while number!=0:
#     digit = number%10
#     number//=10
#     res*=10
#     res+=digit
# else:
#     print(f"Result {res}")

######################

# number = int(input("Enter number : "))
# res=0
# while number!=0:
#     number//=10
#     res+=1
# else:
#     print(res)

# # Завдання 1

# a = int(input("Enter a : "))
# b = int(input("Enter b : "))

# if b<a:
#     temp = b
#     b=a
#     a=temp

# while a<b:
#     print(a)
#     a+=1

# # Завдання 2

# a1 = int(input("Enter a : "))
# b1 = int(input("Enter b : "))

# if b1<a1:
#     temp1 = b1
#     b1=a1
#     a1=temp1

# while a1<b1:
#     if a1%2==0:
#         print(a1)
#     a1+=1


# # Завдання 3

# a2 = int(input("Enter a : "))
# b2 = int(input("Enter b : "))

# if b2<a2:
#     temp2 = b2
#     b2=a2
#     a2=temp2

# while a2<b2:
#     if a2%2==1:
#         print(a2)
#     a2+=1


# # Завдання 4

# a3 = int(input("Enter a : "))
# b3 = int(input("Enter b : "))
# order = int(input("Enter order : "))

# if b3<a3:
#     temp3 = b3
#     b3=a3
#     a3=temp3

# if order==1:
#     while a3<b3:
#         print(a3)
#         a3+=1
# elif order==2:
#     while b3>a3:
#         print(b3)
#         b3-=1
# else:
#     print("Inccorect input")

# # Завдання 5


# a4 = int(input("Enter a : "))
# b4 = int(input("Enter b : "))

# if b4<a4:
#     temp4 = b4
#     b4=a4
#     a4=temp4

# while a4<b4:
#     if a4%2==1:
#         print(a4)
#     a4+=1


# # Завдання 6

# a5 = int(input("Enter a : "))
# b5 = int(input("Enter b : "))
# temp5 = a5

# if b5<a5:
#     temp5 = b5
#     b5=a5
#     a5=temp5

# while a5<b5:
#     if a5%2==0:
#         print(a5)
#     a5+=1

# print("\n")

# while b5>temp5:
#     if b5%2==1:
#         print(b5)
#     b5-=1        


# ##############################################
# # завдання 1
# a = int(input("Enter a : "))
# sum = 0

# while a<500:
#     sum+=a
#     a+=1
# print(sum)

# # завдання 2

# x = int(input("Enter x : "))
# y = int(input("Enter y : "))

# print(x**y)

# # # завдання 3

# sum1=0
# num1=1

# while num1<1000:
#     sum1+=num1
#     num1+=1
# print(f"Result = {sum1/999}")

# # # # завдання 4

# a1 = int(input("Enter a1 : "))
# if a1<1 and a1>20:
#     print("Inccorect input")

# sum2=1

# while a1<=20:
#     sum2*=a1
#     a1+=1
# print(f"Result = {sum2}")

# # # завдання 5

# k = int(input("Enter k : "))

# a=1

# while a<=10:
#     print(f"{k} x {a} = {k*a};")
#     a+=1


# ##############################################
# # # # завдання 1

# sum=0
# a=100
# while a<999:
#     if (a%10)==(a//10) or (a//10%10)==(a%10) or (a//10%10)==(a//10):
#         sum+=1

# print(f"Result = {sum}")

# # # # # завдання 2

# sum2=0
# num2=100
# while num2<999:
#     if (num2%10)!=(num2//10) and (num2//10%10)!=(num2%10) and (num2//10%10)!=(num2//10):
#         sum2+=1

# print(f"Result = {sum2}")

# # # # # завдання 3

# num3 = int(input("Enter num3 : "))
# temp = 0
# t=1
# while num3%10!=0:
#     if (num3%10)!=3 and (num3%10)!=6:
#         temp+=(num3%10)*t
#         t*=10
    
#     num3//=10
# print(temp)

# # # # # # завдання 4

# A = int(input("Enter A: "))
# B = int(input("Enter B: "))

# i=1

# while i<A:
#     if A%(i*i)==0 and A%(i*i*i)!=0:
#         print(i)
    
#     i+=1 

# # # # # # завдання 5

# n1 = int(input("Enter num : "))
# s1=0
# while n1%10!=0:
#     s1+=n1%10
#     n1//=10
# if s1**3==n1*n1:
#     print("Yes")
# else:
#     print("No")

# # # # # # завдання 6

n11 = int(input("Enter number : "))
n12=1

while n12<n11:
    if(n12%n11==0):
        print(n11)
    n11+=1


# # # # # завдання 7

# n2 = int(input("Enter num : "))
# n3 = int(input("Enter num3 : "))

# i1=1

# while i1<n3 or i1<n2:
#     if(n3%i1==0 and n2%i1==0):
#         print(i1)
#     i1+=1