class Node:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority
        self.next = None

class PriorityQueue:
    def __init__(self):
        self.head = None

    def insert(self, value, priority):
        new_node = Node(value, priority)
        if self.head is None or priority < self.head.priority:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next is not None and current.next.priority <= priority:
                current = current.next
            new_node.next = current.next
            current.next = new_node

    def remove(self):
        if self.head is None:
            raise Exception("Priority queue is empty")
        else:
            value = self.head.value
            self.head = self.head.next
            return value

    def is_empty(self):
        return self.head is None

pq = PriorityQueue()
pq.insert("task1", 2)
pq.insert("task2", 3)
pq.insert("task3", 1)

while not pq.is_empty():
    print(pq.remove())