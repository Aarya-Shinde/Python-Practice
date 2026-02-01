# Print all elements from the list in reverse

arr = [1,2,3,4]

print(arr[ : :-1]) #with slicing

   # using two pointers
left = 0
right = len(arr) - 1

while left < right:
    arr[left], arr[right] = arr[right], arr[left]
    left += 1
    right -= 1

print(arr) 

# print first n fibonacci numbers

n = 10
a , b = 0 , 1

for x in range(n):
    print(a , end = " ")
    a, b = b, a + b 

#factorial 

n = 5
fact = 1

for x in range(1 , n+1 ):
    fact *= x
    print(fact)
 
#  or with recursion 
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))  # 120


# Prime or not prime

n = 29
is_prime = True

if n < 2:
    is_prime = False
else:
    for i in range(2, n):
        if n % i == 0:
            is_prime = False
            break

print("Prime" if is_prime else "Not Prime")

 
 


