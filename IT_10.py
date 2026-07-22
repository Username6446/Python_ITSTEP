# matrix = [
#     [1,2,3,4],
#     [4,5,6],
#     [7,8,9]
# ]

# print(matrix[1][1])

# for i in matrix:
#     for j in i:
#         print(j, end=" ")
#     print()

# print("a")

# for i in range(len(matrix)):
#     for j in range(len(matrix[i])):
#         print(matrix[i][j], end=" ")
#     print()

# print()

# import random

# row = col = 3
# matrix = []

# for i in range(row):
#     row_matrix = []
#     for i in range(col):
#         row_matrix.append(random.randint(1,20))
#     matrix.append(row_matrix)

# for i in matrix:
#     for j in i:
#         print(j, end=" ")
#     print()


# row_1 = [random.randint(1,20) for i in range(col)]
# row_2 = [random.randint(1,20) for i in range(col)]
# row_3 = [random.randint(1,20) for i in range(col)]
# matrix = [
#     row_1,
#     row_2,
#     row_3
# ]

# print("\n\n\n\n")

import random
row = col = 3
matrix = [[random.randint(1,20) for i in range(col)] for i in range(row)]

for i in matrix:
    for j in i:
        print(j, end="\t")
    print()


sum_ = 0
for i in matrix:
    for j in i:
        sum_+=j
print(f"Sum = {sum_}")



sum_=0
for i in matrix:
    sum_+=sum(i)
print(f"Sum = {sum_}")


min = matrix[0][0]
max = matrix[0][0]
for i in matrix:
    for j in i:
        if(j<min):
            min=j
        elif(j>max):
            max=j
print(f"Min = {min}, Max = {max}")

clone = matrix.copy()
for i in range(len(matrix)):
    clone[i] = matrix[i].copy()



# clone = matrix
print(clone)
print(matrix)

clone[0][0] = 1

print(clone)
print(matrix)

