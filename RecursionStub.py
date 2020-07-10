from recursion.Factorial import Factorial
from recursion.EnglishRuler import EnglishRuler
from recursion.DiskUsage import DiskUsage
from recursion.UniqueElement import UniqueElement
from recursion.Fibonacci import Fibonacci
from recursion.Misl import Misl

#Recursion
'''f = Factorial()
print(f.factorial(3))'''

#English Ruler
'''
e = EnglishRuler()
e.draw_ruler(3, 4)'''

#Disk DiskUsage
'''
u = DiskUsage()
u.disk_usage('/Users/vipinkumar/Documents/Modules/projects/python-projects/data-structure')'''

#Uniquness of elements
'''
a = [1, 2, 2, 3, 4, 5]
u = UniqueElement()
print(u.unique(a, 0, 5))'''

#fibonacci
'''
f = Fibonacci()
print(f.bad_fibonacci(5))
print(f.good_fibonacci(5))'''


#Misleneous
m = Misl()
a = [1, 2, 3, 4, 5]
print(m.linear_sum(a, 3))
print(m.power(4, 3))
print(m.power_optimized(4, 3))
print(m.binary_sum(a, 0, 4))
m.reverse(a, 0, 5)
for i in range(0, a.__len__()):
    print(a[i])


