from heapq import heappush
from heapq import heappop

fruits = []
heappush(fruits, "orange")
heappush(fruits, "apple")
heappush(fruits, "banana")

print(fruits)

heappop(fruits)
print(fruits)
print("Pops the apple and arrange the orange and banana")

# person1 = ("John", "Brown", 42)
# person2 = ("John", "Doe", 42)
# person3 = ("John", "Doe", 24)
#
# print(person1 < person2)
#
# print(person2 < person3)