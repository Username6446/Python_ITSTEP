# test = [True, "Test", 145, 45.2]
# print(test)


colors = ["red", "purple", "yellow", "orange", "blue"]

# print(f"ID : {id(colors)} \t Type :: {type(colors)} \t Length : {len(colors)}")

# print(colors[2])
# colors[2] = "lime"
# print(colors)

# print('yellow' in colors)
# print('lime' in colors)


#                               start:end:step
# print(colors[::2])
# print(colors[0:3:2])
# print(colors[0:len(colors):2])

# i = 0
# while i<len(colors):
#     print(colors[i].upper())
#     i+=1

# for item in colors:
#     print(item)

#                           add new el in end

# print("")
# print(f"Before :: {colors}")
# colors.append("gold")
# print(f"After :: {colors}")
 
#                                   insert
#print("")
# print(f"Before :: {colors}")
# colors.insert(2,"green")
# print(f"After :: {colors}")

#                                  add lists

# print("")
# print(f"Before :: {colors}")
# colors.extend(["green", " brown", "pink"])
# print(f"After :: {colors}")

# #                                   pop el (ind)
# print("")
# print(f"Before :: {colors}")
# colors.pop(2)
# print(f"After :: {colors}")

#                                       remove (name)
# print("")
# print(f"Before :: {colors}")
# colors.remove("red")
# print(f"After :: {colors}")

# #                       Clear all el
# print("")
# print(f"Before :: {colors}")
# colors.clear()
# print(f"After :: {colors}")


# print(f"Index ::{colors.index("red")}")
# for i in range(4):
#     colors.append("red")

# print(f"List :: {colors}")

# #                             count elements 
# # print(colors.count("red"))

# # sort list  a-z
# print(f"List :: {colors}")
# colors.sort()
# print(f"List :: {colors}")

# # sort z-a
# colors.sort(reverse=True)
# print(f"List :: {colors}")


# numbers = [1,3,2]
# print(max(numbers))
# print(min(numbers))
# print(sum(numbers))
# print(sorted(numbers))
# print(sorted(numbers, reverse=True))

# print(numbers)
# clone = numbers
# clone = numbers.copy() 



# print(f"ID :: {id(numbers)}")
# print(f"ID :: {id(clone)}")


# marks = []
# for i in range(5):
#     n = int(input("Enter number :"))
#     marks.append(n)
# print(marks)

# marks = [i for i in range(5)]  # list 0-4
# print(marks)

# marks = [i for i in input("Enter number : ").split(" ")]  
# print(marks)

# marks = [str(i) for i in marks]
# print(",".join(marks))



# # # Завдання 1

# list = [int(i) for i in input("Enter number : ").split(" ")]
# print(f" Sum  = {sum(list)}, Avg = {sum(list)/len(list)}")

# # # # Завдання 2

# list = [int(i) for i in input("Enter number : ").split(" ")]
# num = int(input("Enter special number : "))

# print(f"{list.count(num)} nums")


# # # Завдання 3

# list = [int(i) for i in input("Enter number : ").split(" ")]
# sum=0
# for i in list:
#     if(i>0):
#         sum+=i

# print(f" Sum  = {sum}")


# # Завдання 4


# list = [int(i) for i in input("Enter number : ").split(" ")]
# count = 0
# for i in list:
#     if(i%2==0):
#         count+=1
# print(f"Count even  = {count}")

# # Завдання 6

# list = [int(i) for i in input("Enter number : ").split(" ")]
# temp = []
# for j in list:
#     if(temp.count(j)<1):
#         temp.append(j)
# print(temp)

# #

# # Завдання 1

list = []
for i in range(10):
    value = int(input("Enter mark: "))
    list.append(value)
while True:
    ch = int(input("Enter choice (1 - out marks, 2 - remark, 3 - is bursary? 0 - end :: "))
    if ch==0:
        print("End")
        break
    elif ch==1:
        print(list)
    elif ch==2:
        a = int(input("Enter index of element ::"))
        b = int(input("Enter element to input ::"))
        list.insert(a,b)
    elif ch==3:
        print("Yes bursary") if (sum(list)/len(list))>=10.7 else print("No bursary")
    else:
        print("Incorrect input")

# # Завдання 2

list = []
for i in range(12):
    value = int(input(f"Enter wage for mounth №{i+1}: "))
    list.append(value)

print(f"Max wage in mounth №{list.index(max(list))+1}\n Min wage in mounth №{list.index(min(list))+1}")

# # # Завдання 3

list = []
for i in range(12):
    value = int(input(f"Enter wage for mounth №{i+1}: "))
    list.append(value)

a = int(input("Enter start ::"))-1
b = int(input("Enter end ::"))-1
copy = list[a:b+1]
ma = max(copy)
mi = min(copy)


print(f"Max wage in mounth №{copy.index(ma)+1}\n Min wage in mounth №{copy.index(mi)+1}")


# # # Завдання 4
n = int(input("Enter length: "))
list = []
for i in range(n):
    value = float(input("Enter num: "))
    list.append(value)

sum = 0
sum2 = 1
for i in list:
    if i<0:
        sum+=i

for i in range(1,n):
    if i%2==0:
        sum2*=list[i]

sum1 = 1
for i in range(list.index(min(list)), list.index(max(list))):
    sum*=list[i]
##
i = 0
temp_f = 0
temp_l = 0
while n>i:
    if(list[i]<0):
        temp_f = i
        break
    i+=1
i=n-1
while i>0:
    if(list[i]<0):
        temp_l = i
        break
    i-=1
##
sum3 = 0
for i in range(temp_f, temp_l):
    sum3+=list[i]

print(f"Sum1 = {sum}, Product1 = {sum1} Sum2 = {sum2}, Product2 = {sum3}")