from itertools import permutations
from itertools import combinations
from itertools import combinations_with_replacement

# #A = [[1, 2, 3, 4], [5, 6, 7, 8]]
# #print(A)

# '''
# N = int(input())
# n = N%2
# print(N)
# print(n)
# if n != 0:
#     print("Weird")
# elif n == 0 and N <= 5 and N >= 2:
#     print("Not Weird")
# elif n == 0 and N <= 20 and N >= 6:
#     print("Weird")
# elif n == 0 and N > 20:
#     print("Not Weird")'''

# '''
# n = int(input())
# i = 0
# while i < n :
#     print(i*i)
#     i = i+1



# # Checking if year is leap or not
# def is_leap(year):
#     leap = False

#     # Write your logic here

#     if year%4 == 0:
#         if year%100 == 0:
#             if year%400 == 0:
#                 leap = True;
#             else:
#                 leap = False;
#         else:
#             leap = True
#     else:
#         leap = False

#     return leap

# year = int(input())
# print(is_leap(year))
# '''
# '''
# #Range Function
# a = range(0, 10)
# print(list(a))'''
# '''
# n = int(input())
# for i in range(1, n+1):
#     print(i, end='')'''

# '''
# # Permutations of a string with given value in numbers
# st = input()
# s = st.split(' ')
# print (s)
# n = list(permutations(s[0], int(s[1])))
# print(n)
# sta = []
# i = 0
# while i < n.__len__():
#     sta.insert(i, ''.join(n[i]))
#     i+=1

# sta.sort()

# for i in sta:
#     print(i)'''

# '''
# # Combinations of a string with given value in numbers
# st = input()
# s = st.split(' ')
# print (s)
# n = list(combinations(s[0], int(s[1])))
# print(n)
# sta = []
# i = 0
# while i < n.__len__():
#     sta.insert(i, ''.join(n[i]))
#     i+=1

# sta.sort()

# for i in sta:
#     print(i)'''

# # Combinations of a string with given value in numbers
# '''st = input()
# s = st.split(' ')
# print (s)
# n = list(combinations_with_replacement(s[0], int(s[1])))
# print(n)
# sta = []
# i = 0
# while i < n.__len__():
#     sta.insert(i, ''.join(n[i]))
#     i+=1

# sta.sort()

# for i in sta:
#     print(i)'''



# '''Power '''
# print(2**10)
# print(6/3)
# print(7//3)
# print(7%3)

# '''List Examples '''

# myList1 = [1, 2, 3, 4, True, "Vipin"]
# print(myList1)
# #in operator
# print(4 in myList1)
# #len operator
# print(len(myList1))

# myList2 = [20, 5, 6, 7, 8]
# #Cancatenation
# myList = myList1 + myList2
# print(myList)
# #Repetition of elements 
# print(myList*5)

# #slicing
# print(myList1[0])
# print(myList1[5])
# print(myList1[1:5])
# print(myList1[0:])
# print(myList1[:5])
# print(myList1[:])

# #append
# myList1.append(10)
# print(myList1)

# #insert
# myList1.insert(5, 20)
# print(myList1)

# #pop
# print(myList1.pop())
# print(myList1.pop(5))

# #sort
# myList3 = [20, 5, 6, 7, 8]
# myList3.sort()
# print(myList3)
# myList3.reverse()
# print(myList3)
# del myList3[4]
# print(myList3)
# print(myList3.index(7))
# print(myList3.count(7))
# myList3.remove(7)
# print(myList3)

# print((54).__add__(21))

# #range
# print(range(10))
# print(list(range(10)))
# print(range(5, 10))
# print(list(range(5, 10)))
# print(list(range(10, 1, -2)))

# '''String example'''
# str = "Vipin Kumar"
# print(str)
# print(str[3])
# print(len(str))
# print(str*2)
# print(str.upper())
# print(str.lower())
# print(str.center(3))
# print(str.find('n'))
# print(str.count('n'))
# print(str.split('n'))