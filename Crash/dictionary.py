empty_dict = {}
another_empty_dict = dict()

students = {
    'name': 'Aarya',
    'Age': '21',
    'grade': 'A'
}

print(students['Age'])
print(students['name'])

print(students.get('name'))

students['Mother'] = 'Usha' #adding a key 
print(students)

print(students.pop('Age'))
print(students)






#  Create dictionary from lists
keys = ['name', 'age', 'grade']
values = ['John', 20, 'A']
student = {k: v for k, v in zip(keys, values)}
print(student)  

# {'name': 'John', 'age': 20, 'grade': 'A'}

# Squares dictionary
squares = {x: x**2 for x in range(1, 6)}
print(squares) 

 # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Filter dictionary

scores = {'John': 85, 'Alice': 92, 'Bob': 78, 'Eve': 95}
high_scorers = {k: v for k, v in scores.items() if v >= 90}
print(high_scorers)  
# {'Alice': 92, 'Eve': 95}