# !5 = 5 * !4
# !4 = 4 * !3
# !3 = 3 * !2
# !2 = 2 * !1
# !1 = 1
# !0 = 1


# def fact(n):
#     if n==1 or n==0:
#         return 1
#     return n * fact(n - 1)

# print(fact(5))



# def printRange(a,b):
#     print(a, end="\t")
#     if a==b:
#         print()
#         return
#     return printRange(a+1,b)

# printRange(1,10)

# # Завдання 1

# def func1(n,m):
#     if m==1:
#         return n
#     return n*func1(n,m-1) 

# print(func1(5,3))

# # Завдання 2

# def func2(a,b):
#     sum = 0
#     if a==b:
#         return a
#     return a+func2(a+1,b)

# print(func2(1,4))

# # Завдання 3

# def func3(a):
#     if a==0:
#         return ""
#     return "*"+func3(a-1)

# print(func3(4))

# # Завдання 1

# def fact(n):
#     if n==1 or n==0:
#         return 1
#     return n * fact(n - 1)

# print(fact(5))


# # Завдання 2

# def printRange(a,b):
#     print(a, end="\t")
#     if a==b:
#         print()
#         return
#     return printRange(a+1,b)

# printRange(1,10)

# def printReverseRange(a,b):
#     print(b, end="\t")
#     if a==b:
#         print()
#         return
#     return printReverseRange(a,b-1)

# printReverseRange(1,10)

# # Завдання 3

# def func3(a):
#     if a<10:
#         print(a, end="")
#     else:
#         print(a % 10, end="")
#         func3(a//10)

# func3(1234)

# # # Завдання 4
# def func4(a):
#     if a==1 or a<10: # a<10
#         return 1
#     return 10*func4(a//10) 

# def func5(a):
#     if a<10:
#         return a
#     return a//func4(a) + func5(a%func4(a))
# print(func5(12))


# # # Завдання 5

# def func6(a):
#    if a==0:
#        return ""
#    print("(", end="")
#    return func6(a-1)+")"

# print(func6(4))


# # # # Завдання 3

# def func3(n, start=0, end=0):
#     if end == 0:
#         end = len(n)-1
#     elif start>=end:
#         return True
#     if n[start] != n[end]:
#         return False
#     return func3(n, start+1, end-1)
# list = [1,2,3,2,1]
# print(func3(list))

# # # # Завдання 4