# while True:
#     choice = input("Enter letter :: ")
#     size = int(input("Enter size :: "))
#     if(choice=="end"):
#         break
#     elif(choice=="a"):
#         print("==========a==========")
#         for i in range(size):
#             for j in range(size):
#                 if(j>=i):
#                     print("*", end=" ")
#                 else:
#                     print(" ", end=" ")
#             print("")        

#     elif(choice=="b"):
#         print("==========b==========")
#         for i in range(size):
#             for j in range(size):
#                 if(j<=i):
#                     print("*", end=" ")
#                 else:
#                     print(" ", end=" ")
#             print("") 
#     elif(choice=="v"):
#         print("==========v==========")
#         for i in range(size):
#             for j in range(size):
#                 if(j>=i and i+j<size):
#                     print("*", end=" ")
#                 else:
#                     print(" ", end=" ")
#             print("") 
#     elif(choice=="g"):
#         print("==========g==========")
#         for i in range(size):
#             for j in range(size):
#                 if(j<=i and size-1<=i+j):
#                     print("*", end=" ")
#                 else:
#                     print(" ", end=" ")
#             print("") 
#     elif(choice=="d"):
#         print("==========d==========")
#         for i in range(size):
#             for j in range(size):
#                 if((j<=i and size-1<=i+j) or (j>=i and i+j<size)):
#                     print("*", end=" ")
#                 else:
#                     print(" ", end=" ")
#             print("") 
#     elif(choice=="e"):
#         print("==========e==========")
#         for i in range(size):
#             for j in range(size):
#                 if((j<=i and size>i+j) or (j>=i and i+j>=size-1)):
#                     print("*", end=" ")
#                 else:
#                     print(" ", end=" ")
#             print("") 
#     elif(choice=="j"):
#         print("==========j==========")
#         for i in range(size):
#             for j in range(size):
#                 if(j<=i and size>i+j):
#                     print("*", end=" ")
#                 else:
#                     print(" ", end=" ")
#             print("")
#     elif(choice=="z"):
#         print("==========z==========")
#         for i in range(size):
#             for j in range(size):
#                 if(j>=i and i+j>=size-1):
#                     print("*", end=" ")
#                 else:
#                     print(" ", end=" ")
#             print("")
#     elif(choice=="i"):
#         print("==========i==========")
#         for i in range(size):
#             for j in range(size):
#                 if(size-i>j):
#                     print("*", end=" ")
#                 else:
#                     print(" ", end=" ")
#             print("")
#     elif(choice=="k"):
#         print("==========k==========")
#         for i in range(size):
#             for j in range(size):
#                 if(size-i>j):
#                     print("*", end=" ")
#                 else:
#                     print(" ", end=" ")
#             print("")
        
    


