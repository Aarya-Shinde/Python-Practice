# Take n integers as input and print their sum.
'''
print("Enter numbers you want Add")
n = list(map(int,input().split()))

print("The sum of those numbers is- ")
print(sum(n))
'''

# Find the largest number in a list of n integers.
'''
a = list(map(int,input("Enter numbers to find Largest: ").split()))

a.reverse()
print(a[0], 'is the largest number')
'''

# From a list of numbers, count how many are even and how many are odd.

'''

b = list(map(int, input("Numbers to count Even & Odd").split()))

even = 0
odd = 0

for i in b:
    if i % 2 == 0:
        even +=1
    else:
        odd +=1   
    
print('Even=', even )
print('Odd=', odd)
'''

# Print the list in reverse order (last to first).
'''
n = int(input())
reversed = list(map(int,input().split()))

for i in range(n-1 , -1 , -1):
    print(reversed[i], end= ' ')
'''

# Print how many times each number appears.

