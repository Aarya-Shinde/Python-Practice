# Creating different type of lists
list = [12, 'aarya', 'shinde', 56 ];

print(list);

print(list[2])

list.append("Pikachu")

print(list)

list.pop()

print(list)

list[1] = 'lala';

print(len(list))

list.insert(2, 'saja') #index no then the elmennt

print(list)

list.remove('saja')

print(list)

del list[3]

list.pop()
print(list)

list.append("pika")
list.insert(3, 'abby')
print(list)

list.pop(0)

print(list)

list.sort()
print(list)

list.reverse()
print(list)

print(list[0][2:4])

squares = [x**2 for x in range(1, 10)] ## [[11,, 44,, 99,, 1166,, 2255]]

print(squares)

even = [x for x in range(30) if  x % 3 == 0]

print(even)