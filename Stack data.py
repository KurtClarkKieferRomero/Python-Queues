from collections import deque

class Queue:
    def __init__(self, *elements):
        self._elements = deque(elements)

    def __len__(self):
        return len(self._elements)

    def __iter__(self):
        while len(self) > 0:
            yield self.dequeue()
class Stack(Queue):
    def dequeue(self):
        return self._elements.pop()

#lifo = Stack("1st", "2nd", "3rd")
#for element in lifo:
    #print(element)

lifo = []

lifo.append("1st")
lifo.append("2nd")
lifo.append("3rd")
print(lifo)
print(lifo.pop())

print(lifo.pop())

print(lifo.pop())
print(lifo)