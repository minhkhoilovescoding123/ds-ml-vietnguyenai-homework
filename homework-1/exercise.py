# Ex1: Write a program to count positive and negative numbers in a list
data1 = [-10, -21, -4, -45, -66, 93, 11, -4, -6, 12, 11, 4]

positiveCount = 0
negativeCount = 0

for number in data1:
    if number > 0:
        positiveCount += 1
    elif number < 0:
        negativeCount += 1

print("Exercise 1:")
print(f"Positive number count: {positiveCount}")
print(f"Negative number count: {negativeCount}\n")

# Ex2: Given a list, extract all elements whose frequency is greater than k.
data2 = [4, 6, 4, 3, 3, 4, 3, 4, 3, 8]
k = 3

solution = []
for number in data2:
    frequency = data2.count(number)

    if frequency > k and number not in solution:
        solution.append(number)

print("Exercise 2:")
print(f"Data2: {data2}")
print(f"Solution: {solution}\n")

# Ex3: find the strongest neighbour. Given an array of N positive integers.
# The task is to find the maximum for every adjacent pair in the array.
data3 = [4, 5, 6, 7, 3, 9, 11, 2, 10]

solution = []
for i in range(len(data3) - 1):
    if data3[i] > data3[i + 1]:
        solution.append(data3[i])
    else:
        solution.append(data3[i + 1])

print("Exercise 3:")
print(f"Data3: {data3}")
print(f"Solution: {solution}\n")

# Ex4: print all Possible Combinations from the three Digits
data4 = [1, 2, 3]

print("Exercise 4:")
print(f"Data4: {data4}")
for i in range (len(data4)):
    for j in range (len(data4)):
        for k in range (len(data4)):
            if i!=j and j!=k and i!=k:
                print (f"{data4[i], data4[j], data4[k]}")

# Ex5: Given two matrices (2 nested lists), the task is to write a Python program
# to add elements to each row from initial matrix.
# For example: Input : test_list1 = [[4, 3, 5,], [1, 2, 3], [3, 7, 4]], test_list2 = [[1], [9], [8]]
# Output : [[4, 3, 5, 1], [1, 2, 3, 9], [3, 7, 4, 8]]
data5_list1 = [[4, 3, 5, ], [1, 2, 3], [3, 7, 4]]
data5_list2 = [[1, 3], [9, 3, 5, 7], [8]]

for i in range(len(data5_list1) - 1):
    for j in range(len(data5_list2[i])):
        data5_list1[i].append(data5_list2[i][j])
print("")
print("Exercise 5:")
print(f"Solution: {data5_list1}\n")

# Ex6:  Write a program which will find all such numbers which are divisible by 7
# but are not a multiple of 5, between 2000 and 3200 (both included).
# The numbers obtained should be printed in a comma-separated sequence on a single line.

solution = ""
for i in range(2000, 3201):
    if i % 7 ==0 and i % 5 !=0:
        solution += f"{str(i)},"

print("Exercise 6:")
stripedSolution = solution.strip()
print(f"Solution: {stripedSolution}\n")

# Ex7: Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.
# The numbers obtained should be printed in a comma-separated sequence on a single line.

solution = ""

def all_digit_even(number):
    while number > 0:
        if number % 2 != 0:
            return False
        number //= 10
    return True

for i in range(1000, 3001):
    if all_digit_even(i):
        solution += f"{str(i)},"
    else:
        continue

print("Exercise 7:")
print(f"Solution: {solution}\n")

# Ex8: Let user type 2 words in English as input. Print out the output
# which is the shortest chain according to the following rules:
# - Each word in the chain has at least 3 letters
# - The 2 input words from user will be used as the first and the last words of the chain
# - 2 last letters of 1 word will be the same as 2 first letters of the next word in the chain
# - All the words are from the file wordsEn.txt
# - If there are multiple shortest chains, return any of them is sufficient
