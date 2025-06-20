#log- Taking different types of inputs

# input function always takes input as a string, even output 
    # we need to convert the input to other datatypes for other values

# taking default string input -will store it as a string

name = input("Enter your name: ");
print("Hello", name);

# taking an integer input - by converting the taken string into integer

age = int(input("Enter your Age: "));  #any letters will cause Value error
print("Confirmation, Your age is", age);  

# Taking an float input - by converting the string into float

weight = float(input("Enter your Weight: "));
weight = int(weight) #coverting int type to float
print('Your weight is', weight);

#! Important- Taking multipule inputs at once -
#  by splitting the inputed string and then coverting them to integer one by one

month , year = input("Enter your birth month and year: ").split();

# - .split() breaks that string into parts based on spaces (default separator).

month = int(month)
year = int(year)

print("Sum is:", month+ year)

# Taking Multiple inputs and converting them to int together- 
# we use map() function to convert all input at once

a , b = map(int,input("Enter two numbers: ").split()) #map(int, ...) applies int() to each value in the split input.
print("Sum", a + b)

# Taking a list of inputs rather than individual variables

numbers = list(map(int, input("Enter numbers seprated by space").split()))
print(numbers)



