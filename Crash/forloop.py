# For Loop -iss used when you want to repeat 
# an action for every item in a collection (list, string, range).

# Syntax

# for item in collection: 
    # do something 


# Print all elements of an array
arr = [10, 20, 30]

for x in arr:
    print(x)

# Print only even numbers from array
# 

even = [1 , 2 , 3 , 4]

for x in even:
    if x % 2 == 0:
        print(x)

# Find sum of all numbers
# 
arr = [1, 2, 3 , 59] 
sum = 0

for x in arr:
    sum += x

print(sum)      

# Find largest number in the list


arr = [3, 7, 2, 9 , 23 ,21 ,56 , 2]

# with python libraries-

arr.sort()
print(arr)

print(f'The Largest number is {arr[-1]}')

# without python libraries-

largest_no = arr[0]

for x in arr:
    if x > arr[0]:
        largest_no = x

print(f"Largest Number is {largest_no}")

# FInd the smallest number

no = [12, 5, 8, 3, 17, 1]

# with in built functions
print(min(no))
print(max(no))

# without the libraries

smallest = no[0]

for x in no:
    if x < smallest:
        smallest = x;

print(f"The smallest no is {smallest}")


# difference between the highest and lowest number of list

list = [12, 5, 8, 3, 17, 1, 23, 45, 93, 1, 3, 45, 33, 74 ]

# with min max functions

difference = max(list) - min(list)

print(difference)

