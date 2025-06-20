# 6. Find the maximum of three numbers.

a , b , c = input().split()

#using if else statement 

if int(a) > b & a > c :
    print("A is greatest no of the three");
elif b > a & b > c :
    print("B is greatest no of the three");
elif c > a & c > b :
    print("C is greatest no of the three");
else :
    print("Invalid input");