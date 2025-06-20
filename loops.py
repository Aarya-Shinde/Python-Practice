#Log- Loops

# For loop - when we know how many times to repeat the loop
'''
for i in range(7):
    print("From 0 to 7 range")
    print(i)

print("From 2 to 5, will stop at 4")
for i in range(2 , 5):
    print(i)

print("From 2 to 7 range, skiping 1 one line")
for i in range(2, 16, 2):
    print(i)    

print("From 2 to 8 range, in reverse")

for i in range(10, 2 , -1):   
    print(i)

#looping over a list
fruits = ['apple', 'mango', 'lichi', 'something']
for fruits in fruits:
    print(fruits)    

#looping over a dictionary
grades = {'Aarya': 90, 'Usha': 75}
for name, score in grades.items():
    print(f'{name} has scored {score}')

#for loops inside loops

for i in range(2):
    for j in range(3):
        print(i , j)    

'''

# While loops---

'''count = 0;
while count <= 3:
    print(count);
    count += 1;

password = ""

while password != 'letmein':
    password = input("Enter password")


command = ""
command = input("Enter command")

while command != 'open':
    command = input("Enter password")
    if command == '123':
        print("Welcome");
        pass;
    else:
        break;'''