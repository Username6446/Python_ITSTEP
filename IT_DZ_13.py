# # # # Завдання 1
def func1(n):
    if n%10==0:
        return n
    return max(func1(n//10),n%10)

print(func1(1234))

# # # # # Завдання 2

def func2(n, i=2):
    if n%i==0:
        return False
    if i>=(n//2):
        return True
    return func2(n,i+1)

print(func2(12))

# # # # # Завдання 3

def func3(n, i=2):
    if n%i==0:
        print(i)
        return func3(n//i,i)
    if n//i==0:
        return 
    func3(n,i+1)
    

func3(78)

# # # # Завдання 4

def func4(n, i=1,j=1, m=1):
    if m==n:
        return i
    temp = i
    return func4(n, i=j, j=j+temp, m=m+1)

print(func4(6))
