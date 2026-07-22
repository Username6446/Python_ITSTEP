import re
# # Ex1

def ex1():
    
    try:
        num1 = float(input("Enter number :: "))
        num2 = float(input("Enter number :: "))
        print(f"Result = {num1/num2}")
    except ValueError as msg:
        print(f"ValueError :: message :: {msg}")
    except ZeroDivisionError as msg:
         print(f"ZeroDivisionError :: message :: {msg}")
    finally:
        print("End")


# # Ex2

def ex2():
    list = [10,20,30,40,50]
    ind = input("Enter index(0-4):: ")
    print(ind)
    try:
        ind = int(ind)
        print(ind)
        if 0 > ind:
            raise IndexError("Index can not be negative")
        print(list[ind])
    except ValueError as msg:
        print(f"ValueError :: message :: {msg}")
    except IndexError as msg:
        print(f"IndexError :: message :: {msg}")
    finally:
        print("End")


# # Ex3

def ex3():
    line = input("Enter line :: ")
    try:
        line = list(map(lambda item: int(item), line.split(" ")))
        print(f"Sum = {sum(line)}")
    except ValueError as msg:
        print(f"ValueError :: message :: {msg}")
    finally:
        print("End")

# # Ex4

def ex4():
    num1 = input("Enter number :: ")
    try:
        num1 = int(num1)
        if 0 > num1:
            raise Exception("Не можна обчислити квадратний корінь від'ємного числа")
        print(f"Res = {num1*num1}")
    except Exception as msg:
        print(f"Exception :: message :: {msg}")
    except ValueError as msg:
        print(f"ValueError :: message :: {msg}")
    finally:
        print("End")

# # Ex5
def ex5():
    order = input("Enter information in format ( Хліб, 1.5, 10 ) :: ")
    try:    
        result = order.split(", ")
        result[1] = float(result[1]) 
        result[2] = int(result[2]) 
    except ValueError as msg:
        print(f"ValueError :: message :: {msg}")
    finally:
        print("End")

# # Ex6
import random

def ex6():
    def connect_to_server():
        if random.randint(0,1)==1:
            raise ConnectionError("Помилка підключення")
        else:
            print("Успішне підключення")
    try:
        connect_to_server()
    except ConnectionError as msg:
        print(f"Error :: {msg}")
    finally:
        print("Спробу завершено")

