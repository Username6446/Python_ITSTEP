# # example 1
# number = input("Enter number :: ")
# number = int(number)

# print(f"Number :: {number}")
# print("finally code")


# try:
#     number = input("Enter number :: ")
#     number = int(number)

#     print(f"Number :: {number}")
#     print("finally code")
# except:
#     print("Run block except")

# # example 2
# while True:
        
#     try:
#         test = True
#         number_1 = int(input("Enter number :: "))
#         number_2 = int(input("Enter number :: "))
#         print(f"result :: {number_1} / {number_2} = {number_1/ number_2}")
#         print("End code")
#         # break
#     except ValueError as msg:
#         print(f"Run block ValueError :: message :: {msg}")
#     except ZeroDivisionError as msg:
#         print(f"Run block ZeroDivisionError :: message :: {msg}")
#     except (TypeError, NameError) as msg:
#         print(f"Run block TypeError or NameError :: message :: {msg}")
#     except Exception as msg:
#         print(f"Run block Ecteption :: message :: {msg}")
#     else:
#         print("Finnaly block try -=-> Run block else")
#         break
#     finally:
#         print("Disconnection")


# print("End program")


# def printNumber(number):
#     if number < 0:
#         raise ValueError(f"{number} < 0")
#     if number > 10_000:
#         raise Exception(f"{number} > 10 000")
#     print(f"Print number :: {number}")

    
# while True:
#     try:    
#         number = int(input("Enter value :: "))
#         printNumber(number)
#         break
#     except ValueError as msg:
#         print(f"Run block ValueError :: message :: {msg}")
#     except Exception as msg:
#         print(f"Run block Exception :: message :: {msg}")

# print("End program") 

# # Ex1

def ex1():
    cost = input("Enter cost :: ")
    sale = input("Enter sale :: ")
    try:
        cost = int(cost)
        sale = int(sale)
        print(f"Sum = {cost*(100-sale)/100}")
    except ValueError as msg:
        print(f"ValueError :: message :: {msg}")
    finally:
        print("End")


# # Ex2

def ex2():
    sum = input("Enter dol :: ")
    curs = input("Enter curs :: ")
    try:
        sum = int(sum)
        curs = float(curs)
        if curs==0:
            raise Exception("Курс обміну не може дорівнювати нулю")
        print(f"Eur = {sum*curs}")
    except Exception as msg:
        print(f"ValueError :: message :: {msg}")
    finally:
        print("End")



# # Ex3

def ex3():
    marks = input("Enter marks :: ").split(" ")
    try:
        marks = list(map(lambda item: int(item), marks))
        if len(marks)==0:
            raise ZeroDivisionError
    except ValueError as msg:
        print(f"ValueError :: message :: {msg}")
    except ZeroDivisionError as msg:
         print(f"ZeroDivisionError :: message :: {msg}")
    finally:
        print("End")

# # Ex4


def ex4():
    sum = input("Enter sum :: ")
    try:
        sum = int(sum)
        if sum//10!=0 or sum>=1000:
            raise Exception("Некоректна сума для зняття")
    except Exception as msg:
        print(f"Exception :: message :: {msg}")
    finally:
        print("End")

# # Ex5
def ex5():
    order = input("Enter number of order ( ORD1234 ) :: ")
    try:    
        if order[:3] != "ORD" or not (order[3:].isdigit()):
            raise Exception("Неправильний формат номера замовлення")
    except Exception as msg:
        print(f"Exception :: message :: {msg}")
    finally:
        print("End of checking")

# # Ex6

def ex6():
    sequence = input("Enter sequens of numbers sep be space :: ").split()
    try:
        i=0
        while True:
            if i==len(sequence):
                break
            try:
                sequence[i] = int(sequence[i])
                i+=1
            except ValueError:
                print(f"Warning element {sequence[i]} is missing")
                sequence.pop(i)
                i-=1
                
        print(f"Sum of elements = {sum(sequence)} Average = {sum(sequence)/len(sequence)}")
    except ZeroDivisionError as msg:
        print(f"Error {msg}")
    finally:
        print("End of checking")

ex6()