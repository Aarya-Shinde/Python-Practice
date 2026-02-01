# Print the maximum number

list = [0 , 1 , 3, 5, 7, 2]

max_val = list[0]

for x in list:
    if x > max_val:
        max_val = x

print(max_val)


# Count how many times a letter 

str = "apple"

times = {}

for ch in str:
    if ch in times:
        times[ch] += 1
    else:
        times[ch] = 1

print(times)


# Remove duplicates

list = [1 , 2 ,2,3 ,6,6 ,9]

result =[]

for x in list:
    if x not in result:
        result.append(x)

print(result)     

# Checking if its a palindrome

s = "aarya"

def is_palindrome(s):
    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1

    return True

print(is_palindrome(s))