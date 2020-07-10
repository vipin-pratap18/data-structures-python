from search_algo.BinarySearch import BinarySearch

b = BinarySearch()
data = [2, 4, 5, 7, 8, 9, 12, 14, 17, 19, 22, 25, 27, 28, 33, 37]
target = 22
low = 0
high = 15
#Floor of the division
print((low + high) // 2)
#Normal division
print((low + high) / 2)
print(b.binary_search(data, target, low, high))



