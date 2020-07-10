# List declaration
my_list = []
print(my_list)
my_list = [1, 2, 3]
print(my_list)
my_list = [1, "Hello", 2]
print(my_list)
my_list = ["mouse", [8, 4, 6], ['a']]
print(my_list)

# List Indexing
my_list = ['p', 'r', 'o', 'b', 'e']
print(my_list[0])

new_list = ["happy", [2, 0, 1, 5]]
print(new_list[0][1])
print(new_list[1][3])
# Negative indexes are for access from last
print(my_list[-1])
print(my_list[-2])
#Slicing
my_list = ['p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z']
# elements 3rd to 5th e.g. ==> [index:length]
print(my_list[2:5])
# elements from 0th to -5th, means begining to 4th
print(my_list[:-5])
# elements from 5th to the last
print(my_list[5:])
# elements begining to end
print(my_list[:])
# List modification
odd = [2, 4, 6, 8]
# change first one
odd[0] = 1
print(odd)
# change 2nd to 4th items
odd[1:4] = [3, 5, 7]
print(odd)
# Append one element at last
odd.append(7)
print(odd)
# Append an array at last
odd.extend([9, 11, 13])
print(odd)
#Concatenation
odd = [1, 3, 5]
print(odd + [7, 9, 11, 13])
print(["re"] * 3)
print([2] * 3)

odd = [1, 9]
odd.insert(1, 3)
print(odd)

odd[2:2] = [5, 7]
print(odd)

#Deleting elements
my_list = ['p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z']

del my_list[2]
print(my_list)

del my_list[1:5]
print(my_list)

# del my_list
# print(my_list)

my_list = ['p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z']

my_list.remove('p')
print(my_list)

print(my_list.pop(1))

print(my_list)

print(my_list.pop())
print(my_list)

my_list.clear()
print(my_list)


my_list = [3, 8, 1, 6, 0, 8, 4]
print(my_list.index(8))

print(my_list.count(8))
my_list.sort()
print(my_list)

my_list.reverse()
print(my_list)


#List comparisions
pow2 = [2 ** x for x in range(10)]
print(pow2)

#above code is similar to the below
pow2 = []
for x in range(10):
    pow2.append(2 ** x)

print(pow2)

pow2 = [2 ** x for x in range(10) if x > 5]
print(pow2)

odd = [x for x in range(20) if x % 2 == 1]
print(odd)

mix_list = [x + y for x in ['Python ', 'C '] for y in ['Language', 'Programming']]
print(mix_list)

# List member check
my_list = ['p', 'r', 'o', 'b', 'l', 'e', 'm']

print('p' in my_list)
print('a' in my_list)
print('c' not in my_list)


#iterating through a list
for fruit in ['apple', 'banana', 'mango']:
    print("I like ", fruit)

