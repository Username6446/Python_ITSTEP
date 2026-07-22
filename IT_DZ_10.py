import random 
# # # Завдання 1

list = [int(i) for i in input("Enter number : ").split(" ")]

count = 0
for i in range(len(list)-1):
    if(list[i]<list[i+1]):
        count+=1
print(count)

# # # Завдання 2

list = [int(i) for i in input("Enter number : ").split(" ")]
res = []

for i in list:
    if(list.count(i)==1):
        res.append(i)

print(res)

# # Завдання 3

list = [int(i) for i in input("Enter number: ").split()]
l = 1         
temp = 1        
ind = 0         
res = []        

for i in range(1, len(list)):
    if list[i] > list[i-1]:
        temp += 1
        if temp>l:
            l = temp
            ind = i-l+1
    else:
        temp = 1  

res = list[ind:ind + l]

print("length:", l)
print("res:", res)


# # # # Завдання 4

list = [int(i) for i in input("Enter number: ").split()]
number = int(input("Enter N : "))
number=number%len(list)
res = []

for i in range(len(list)-number, len(list)):
    res.append(list[i])
for i in range(len(list)-number):
    res.append(list[i])
print(res)

# # # Завдання 5


l1 = [random.randint(1,10) for i in range(5)]
l2 = [random.randint(1,10) for i in range(5)]
print(l1,l2)
res = []
res.extend(l1)
res.extend(l2)
print(f"Res = {res}")
for i in res:
    count = res.count(i)
    for j in range(count-1):
        res.remove(i)
print(f"Res = {res}")
res.clear()
for i in l1:
    for j in l2:
        if(i==j and res.count(i)<=1):
            res.append(i)
print(f"Res = {res}")
res.clear()
for i in l1:
    if l2.count(i)==0:
        res.append(i)
for i in l2:
    if res.count(i)==0 and l1.count(i)==0:
        res.append(i)
print(f"Res = {res}")
res.clear()
max_1 = max(l1)
max_2 = max(l2)
min_1 = min(l1)
min_2 = min(l2)
res = [max_1, max_2, min_1, min_2]
print(f"Res = {res}")

# # # Завдання 6

list = [int(i) for i in input("Enter number: ").split()]
list.sort()
print(list)
res = []

if res.clear==res:
    print(4)
for i in range(len(list)):
    if len(list)==len(res):
        break
    res.append(list[i])
    if len(list)==len(res):
        break
    res.append(list[len(list)-i-1])
print(res)

    
