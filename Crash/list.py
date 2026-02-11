# List - is a  ordered collection of diff. data types and is mutable. 
#  allows duplicate members.
#  []

# Tuple - ordered collection that is immutable. 
#  allows duplicate 
#  ()

# Set - unordered collection that is mutable.
#  unique members only
# {}

# Intializing empty list
my_list = [1]
another_list = list()
print(another_list)

# List with elements
numbers = [1,2,3,4,5]
mixed = [1 ,"hello" , 3.14, True] #icludes different types
nested = [[1,2],[2,3],[4,6]] #List of lists

print(nested)

# modifying lists

numbers = [1,2,3,4,5,2 ,5,8,4]

numbers[1] = 10
print(numbers) #[1, 10, 3, 4, 5, 2, 5, 8, 4]

# Add elements
numbers.append(6) #will add at end
numbers.insert(1, 26) #insert at position 1, pushes the existing number back 
numbers.extend([14,"lala"]) #adds multiple at the back

print(numbers) 

# Remove elements

numbers.remove(10)   # Remove first occurrence of 10
popped = numbers.pop()   # Remove and return last element
popped_at = numbers.pop(0)  # Remove at specific index
del numbers[0]           # Delete by index
numbers.clear()          # Remove all elements


# ==========================================
# COMMON LIST METHODS
# ==========================================
nums = [3, 1, 4, 1, 5, 9, 2, 6]
# Sorting
nums.sort()              
print(nums)              
# Sort in place (modifies original)
# [1, 1, 2, 3, 4, 5, 6, 9]
nums.sort(reverse=True)  # Sort descending
print(nums)              
# [9, 6, 5, 4, 3, 2, 1, 1]
# sorted() - returns new sorted list (doesn't modify original)
original = [3, 1, 4]
sorted_list = sorted(original)
print(original)      
# [3, 1, 4] - unchanged


print(sorted_list)   # [1, 3, 4] - new sorted list
# Other useful methods
nums = [1, 2, 3, 2, 4]
print(nums.count(2))     # 2 - how many times 2 appears
print(nums.index(3))     # 2 - index of first occurrence of 3
nums.reverse()           # Reverse in place
print(len(nums))         # 5 - length of list
# ==========================================
# LIST COMPREHENSION (IMPORTANT!)
# ==========================================
# Traditional way
squares = []
for x in range(10):
    squares.append(x**2)
# List comprehension (preferred!)
squares = [x**2 for x in range(10)]
print(squares)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
# With condition
evens = [x for x in range(20) if x % 2 == 0]
print(evens)  # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
# More examples
nums = [1, 2, 3, 4, 5]
doubled = [x * 2 for x in nums]           # [2, 4, 6, 8, 10]
strings = [str(x) for x in nums]          # ['1', '2', '3', '4', '5']
filtered = [x for x in nums if x > 2]     # [3, 4, 5]






