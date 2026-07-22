import re
# ex1
def func1():
    list_line = []
    for i in range(3):
        line = input("Enter line :: ")
        list_line.append(line)
    with open("16_DZ_files/data.txt", "w") as file:
            file.write("\n".join(list_line))

# ex2
def func2():
    try:
        with open("16_DZ_files/data.txt", "r") as file:
            file.readline()
            print(file.readline())
    except FileExistsError as msg:
        print(msg)


# ex3

def func3():
    with open("16_DZ_files/filtered.txt", "w") as filtered:
        with open("16_DZ_files/data.txt", "r") as data:
            lines = data.readlines()
            for i in lines:
                if (i).count("Python")>0:
                    filtered.writelines(i)


# ex4

def func4():
    file_name = input("Enter file name :: ")
    with open("16_DZ_files/cleaned.txt", "w") as filtered:
        with open(f"16_DZ_files/{file_name}.txt", "r") as data:
            for line in data:
                list = []
                for ch in line:
                    if ch.isdigit():
                        continue
                    else:
                        list.append(ch)
                filtered.write("".join(list))

# 5

def func5():
    list_words = []
    list_count = []
    try:
        with open("16_DZ_files/log.txt", 'r') as file:
            text = file.read()
            words = re.findall(r"\w+", text)
            print(words)
            for i in range(len(words)):
                flag = True
                for j in range(i):
                    if words[i]==words[j]:
                        flag==False
                        break
                if flag:
                    list_words.append(words[i])
                    list_count.append(words.count(words[i]))
            for i in range(len(list_words)):
                print(list_words[i], " : ", list_count[i])
            with open("16_DZ_files/word_stats.txt", 'w') as file:
                for i in range(10):
                    max_ = max(list_count)
                    index_ = list_count.index(max_)
                    file.write(f"{list_words[index_]} :: {list_count[index_]} \n")
                    list_words.pop(index_)
                    list_count.pop(index_)
    except Exception as msg:
        print(msg)



# ex6

def func6():
    with open("16_DZ_files/cleaned.txt", "w") as filtered:
        with open(f"16_DZ_files/data.txt", "r") as data:
            lines = data.readlines()
            print(lines)
            for i in range(len(lines)):
                filtered.write(lines[len(lines)-i-1])
