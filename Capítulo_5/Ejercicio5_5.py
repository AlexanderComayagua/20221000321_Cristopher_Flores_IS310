class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularList:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def insert(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
            new_node.next = self.head
        else:
            new_node.next = self.head
            self.tail.next = new_node
            self.tail = new_node

    def remove(self):
        if self.is_empty():
            return None
        data = self.head.data
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.tail.next = self.head
        return data

    def peek(self):
        if self.is_empty():
            return None
        return self.head.data

class Stack:
    def __init__(self):
        self.list = CircularList()

    def push(self, data):
        self.list.insert(data)

    def pop(self):
        return self.list.remove()

    def peek(self):
        return self.list.peek()

class Queue:
    def __init__(self):
        self.list = CircularList()

    def insert(self, data):
        self.list.insert(data)

    def remove(self):
        return self.list.remove()

    def peek(self):
        return self.list.peek()

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.peek())  # Output: 3
print(stack.pop())  # Output: 3
print(stack.peek())  # Output: 2

queue = Queue()
queue.insert(1)
queue.insert(2)
queue.insert(3)
print(queue.peek())  # Output: 1
print(queue.remove())  # Output: 1
print(queue.peek())  # Output: 2