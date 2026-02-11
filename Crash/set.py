practise_set = {1,2,3,4}

practise_set.add(7)
practise_set.update([90,42])
print(practise_set)

practise_set.pop()
practise_set.pop()
print(practise_set)

practise_set.clear()
print(practise_set)

# removing duplicates from the list by turing it into a set

duplicate_list = [1, 2, 2, 3, 4, 8, 9, 9]
unique_numbers = list(set(duplicate_list))
print(unique_numbers)

# set operations

set1 ={1 ,2 ,3,4,4}
set2 = {8,7,5,3}

print(set1, set2)  #{1, 2, 3, 4} {8, 3, 5, 7}

# Union - all elements from both sets
print(set1 | set2) #{1, 2, 3, 4, 5, 7, 8}
print(set1.union(set2)) # same as above

# Intersection
print(set1 & set2) #  {3}
print(set1.intersection(set2)) #same as above

# Difference
print(set2 - set1) #{8, 5, 7}
print(set1.difference(set2)) # in set1 but not in set2

# Symmetric difference
print(set1 ^ set2) #{1, 2, 4, 5, 7, 8}
print(set1.symmetric_difference(set2)) #same as above

# Subset and Supersets

set_a = {1, 2, 3}
set_b = {1, 2, 3, 4, 5}

print(set_a.issubset(set_b))    # True - all of set_a is in set_b
print(set_b.issuperset(set_a))  # True - set_b contains all of set_a

common = set1 & set2
print(common)



