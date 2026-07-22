# # Ex.1

a = int(input("Enter num1 :: "))
b = int(input("Enter num2 :: "))

res=0

for i in range(a,b+1):
    for j in range(1,i+1):
            if(i%j==0):
                res+=1
    print(f"Дільники для числа {i} =  {res}")
    res=0

# # # Ex.2
flag=True

for i in range(3,1001):
    for j in range(2,i):
          if(i%j==0):
               flag=False
    if(flag):
        print(i, end=", ")
    flag=True

            
# # # Ex.3
time=0
for i in range(0,1000):
    if(i<10):
        print(f"00{i}", end="\t")
    elif(i<100):
        print(f"0{i}", end="\t")
    else:
        print(i, end="\t")
    time+=3

hours = time//3600
minutes = (time-(hours*3600))//60

print(f"\n\n{hours} hours, {minutes} minutes, {time-(minutes*60)} seconds")
# # # Ex.4

result=0

for i in range(12):
    pay = int(input("Enter Березень :: "))
    pay1 = int(input("Enter Квітень :: "))
    pay2 = int(input("Enter Травень :: "))
    sum=pay+pay1+pay2
    print(f"Worker{i+1} sum = {sum}\n")
    result+=sum
print(f"All sum = {result}")

# # # Ex.5


mounth = int(input("Enter mounth number(1-12):: "))
dayOfWeek = int(input("Enter a number day of week(1-7):: "))

print("\t\t\t")
match mounth:
    case 1:
        print("January")
    case 2:
        print("February")
    case 3:
        print("March")
    case 4:
        print("April")
    case 5:
        print("May")
    case 6:
        print("June")
    case 7:
        print("July")
    case 8:
        print("August")
    case 9:
        print("September")
    case 10:
        print("October")
    case 11:
        print("November")
    case 12:
        print("December")

print(f"Mon\tTu\tWe\tTh\tFr\tSa\tSu")
dayOfWeek-=1
for i in range(dayOfWeek):
    print("\t",end="")

for i in range(1,32):
    print(i) if (i+dayOfWeek)%7==0 else print(i, end="\t") 


# # # Ex.6

size = int(input("Enter number odd):: "))

for i in range(size):
    for j in range(size):
        if(i==size//2 or j==size//2 or i==j or j==size-i-1):
            print("*", end=" ")
        else:
            print("  ", end="")
    print("")