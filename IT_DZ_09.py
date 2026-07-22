# # # Завдання 1

list = [int(i) for i in input("Enter number : ").split(" ")]

odd = 0
even = 0
for i in list:
    if(i%2==0):
        even+=1
    else:
        odd+=1
        
print(f" Odd  = {odd}, Even = {even}")


# # # Завдання 2

list = [int(i) for i in input("Enter number : ").split(" ")]
print(f"Max = {max(list)}, Min = {min(list)}")


# # # Завдання 3
import random
n = int(input("Enter size : "))
list = [(random.random()-0.5)*100//10 for i in range(n)]
print(list)

list.sort()
print(list)
temp = 0
for i in range(n-1):
    if (list[i]<0 and list[i+1]>=0):
        temp=i+1
        
list1 = list[:temp]
list2 = list[temp:]

list2 = [x for x in list2 if x!=0]

print(f"Max negative: {max(list1) if list1 else '-'}")
print(f"Min positive: {min(list2) if list2 else '-'}")
print(f"Number of negatives: {len(list1)}")
print(f"Number of positives: {len(list2)}")
print(f"Number of zeros: = {list.count(0)}")

# # # # Завдання 4
list = [int(i) for i in input("Enter number : ").split(" ")]
num = int(input("Enter number : "))

for i in list:
    if i<num:
        list.remove(i)
print(list)

# # Завдання 5

ex = input("Enter arithmetic expression : ")

operators = ['+', '-', '*', '/']
op = '0'
for char in ex:
    if char in operators:
        op = char
        break

numbers = ex.split(op)

num1 = float(numbers[0])
num2 = float(numbers[1])

if op == '+':
    result = num1 + num2
elif op == '-':
    result = num1 - num2
elif op == '*':
    result = num1 * num2
elif op == '/':
    result = num1 / num2    
print(result)
        

# # # Завдання 6

list = [int(i) for i in input("Enter number : ").split(" ")]
temp1_1 = [] # -3, -2
temp1_2 = [] # 1, 4
temp2_1 = [] # 4, 1, 0, 5
temp2_2 = [] # 0, 2, 3, 4

res = [0]*len(list)

for i in range(len(list)):
    if list[i]<0:
        temp1_1.append(list[i])
        temp1_2.append(i)
    else:
        temp2_1.append(list[i])
        temp2_2.append(i)

temp2_1.sort()
for i in range(len(temp1_2)):
    res[temp1_2[i]] = temp1_1[i]


for i in range(len(temp2_2)):
    res[temp2_2[i]] = temp2_1[i]
print(res)