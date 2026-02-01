# 5. Check whether a number is even or odd.  

number= int(input("Enter a Number: "))


if number%2 == 0:
    print("Even number")
elif number%2 == 1:
    print("Odd number")
else:
    print("'Invalid Input")




# rEMOVE dUPLICATE VALUES

list = [3, 9 , 23, 92, 3 ]

result = []

for x in list:
    if x not in result:
        result.append(x)

print(result)
