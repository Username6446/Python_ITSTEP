# open
# read 
# write
# close

# "C:\Users\Іван\Desktop\main.css"
# "../main.css"

# file = open(r"../main.css")
# allText = file.read()
# print(allText)
# file.close()

url = "files/file.txt"

# try:
#     url = "../text.txt"
#     file = open(url)
#     print(file.read())
# except Exception as msg:
#     print(msg)
# finally:
#     file.close()
#     pass

# with open(url) as file:
#     print(file.readline())
#     file.seek(1)
#     print(file.readlines())
#     file.seek(0)
#     print(file.read(5))
#     file.seek(0)
#     i=1
#     for line in file:
#         print(i, line)
#         i+=1

# with open("files/file1.txt", "w+") as file:
#     for i in range(3):
#         file.write(f"Test line {i+1}\n")

# numbers = [1,2,3,4,5,6,4,5]
# numbers = map(lambda x: str(x) + "\n", numbers)
# with open("files/file2.txt", "w+") as file:
#     file.writelines(numbers)

# words = map(lambda x : x + "\n", "Сніг Дощ Хмара Сонце". split())
# with open("files/words.txt", "w+", encoding="utf-8") as file:
#     file.writelines(words)
#     file.seek(0)
#     print(file.read())





# # Ex1

def ex1():
    with open("files/output.txt", "w") as file:
        file.write("Hello, world!")

# # Ex2
def ex2():
    with open("files/output.txt", "r") as file:
        print(file.read())


# # Ex3
def ex3():
    with open("files/data.txt", "w") as file:
        file.write("Hello, world!\nHello1")
    file2 = open("files/data.txt", "r")
    with open("files/backup.txt", "w") as file:
        for line in file2:
            file.write(line)
    
# # Ex4

def ex4():
    counter = 0
    with open("files/data.txt", "r") as file:
        for line in file:
            counter+=1
            # file.write(line)
    
    print(counter)

# # Ex5
import re
def ex5():
    counter = 0
    words = 0
    chars = 0
    s = ""
    # list = 0
    with open("files/data.txt", "r") as file:
        for line in file:
            counter+=1
        file.seek(0)
        l = file.readlines()
        for intr in l:
            s += str(intr)
        words = re.findall(r"\w+", s)
        chars = re.findall(r"\w", s)
    print(counter)
    print(len(words))
    print(len(chars))
    print(words)
    print(chars)
    
# # Ex6

def ex6():
    file1 = open("files/encrypted.txt", "w")
    with open("files/data.txt", "r") as file:
        for line in file:
            list = []
            for char in line:
                if 'a' <= char <= 'z':
                    new_char = 'a' if char == 'z' else chr(ord(char) + 1)
                    list.append(new_char)
                elif 'A' <= char <= 'Z':
                    new_char = 'A' if char == 'Z' else chr(ord(char) + 1)
                    list.append(new_char)
                else:
                    list.append(char)
            file1.write(''.join(list))
    file1.close()
    print(ord('a'))