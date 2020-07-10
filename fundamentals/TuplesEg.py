# A tuple in Python is similar to a list. The difference between the two is that we cannot change the elements of a tuple once it is assigned whereas we can change the elements of a list.

my_tuple = ()
print(my_tuple)

my_tuple = (1, 2, 3)
print(my_tuple)

my_tuple = (1, "Hello", 3.4)
print(my_tuple)

my_tuple = ("mouse", [8,4,6], (1, 2, 3))
print(my_tuple)
print(my_tuple[0])
# Error of no assignment allowed in tuple
# my_tuple[0] = "New Value"

# tuple without parenthesis
my_tuple = 3, 4.6, "dog"
print(my_tuple)

