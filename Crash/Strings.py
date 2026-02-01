# ord() function gives back unicode of the single string digit

# name = "A"

# d = ord(name)

# print(type(d), d)

name = "Aarya";
age = 21;

# Concatenate
# print('Hello, I am ' + name + ' of age ' + str(age));

# Argument by position
# print("Hello, I am {name} who is {age} this year".format(name = name , age = age)) 

# F- Strings
print(f"Hello, I'm {name} and my age is {age}.")

# **************** STRING METHODS *******************

s = "hello pikachu"

# Capitalizes string 
print(s.capitalize())

# makes it all uppercase
print(s.upper())

# makes it all lowercase
print(s.lower())

#swap cases by making upper lowers and lowers upper
print(s.swapcase())

# get length, can be used on lists, set etc-- counts space too
print(len(s))

#Replaces something with something
print(s.replace('pikachu', 'everyone'))

# Counts the character
print(s.count('h'))
       # or 

ch = 'e'
print(s.count(ch))




