from dataclasses import dataclass
from collections import deque
from heapq import heappop, heappush
@dataclass
class Message:
    event: str
class PriorityQueue:
    def __init__(self):
        self._elements = []

    def enqueue_with_priority(self, priority, value):
        heappush(self._elements, (priority, value))

    def dequeue(self):
        return heappop(self._elements)

wipers = Message("Windshield wipers turned on")
hazard_lights = Message("Hazard lights turned on")

#wipers < hazard_lights #can't compare since they are strings that are uninstructed

CRITICAL = 3
IMPORTANT = 2
NEUTRAL = 1
messages = PriorityQueue()
messages.enqueue_with_priority(CRITICAL, wipers)
messages.enqueue_with_priority(IMPORTANT, hazard_lights)
