# Day 8 Practice: Basic Data Structures


class Stack:
    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)

    def pop(self):
        if self.is_empty():
            return None
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0


class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, value):
        self.items.append(value)

    def dequeue(self):
        if self.is_empty():
            return None
        return self.items.pop(0)

    def is_empty(self):
        return len(self.items) == 0


if __name__ == "__main__":
    stack = Stack()
    stack.push(10)
    stack.push(20)
    print("Stack peek:", stack.peek())
    print("Stack pop:", stack.pop())

    queue = Queue()
    queue.enqueue("first")
    queue.enqueue("second")
    print("Queue dequeue:", queue.dequeue())
