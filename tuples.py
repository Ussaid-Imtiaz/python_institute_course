# Example 1
tuple_1 = (1, 2, 3)
for elem in tuple_1:
    print(elem)

# Example 2
tuple_2 = (1, 2, 3, 4)
print(5 in tuple_2)
print(5 not in tuple_2)

# Example 3
tuple_3 = (1, 2, 3, 5)
print(len(tuple_3))

# Example 4
tuple_4 = tuple_1 + tuple_2
tuple_5 = tuple_3 * 2

print(tuple_4)
print(tuple_5)

my_tuple = tuple((1, 2, "string"))
my_tuple[1]
print(my_tuple)

print()

my_list = [2]
print(my_list)    # outputs: [2, 4, 6]
print(type(my_list))    # outputs: <class 'list'>
tup = tuple(my_list)
print(tup)    # outputs: (2, 4, 6)
print(type(tup))    # outputs: <class 'tuple'>


tup = 1, 2, 3
a, b, c = tup

print(a * b * c)

tup = (1, 2, 4, 8)
tup = tup[1:-1]
print(tup)
tup = tup[0]
print(tup)
print(type(tup))

tup = (1,) + (1,)
tup = tup + tup
print(len(tup))

tup = (1,2)
tup[0] = tup[1] + tup[0]

print(tup)