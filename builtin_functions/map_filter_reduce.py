#map
nums = [1, 2, 3, 4]
squared = list(map(lambda x: x**2, nums))
print(squared)

#filter
even = list(filter(lambda x: x % 2 == 0, nums))
print(even)


#reduсe
from functools import reduce

total = reduce(lambda x, y: x + y, nums)
print(total)