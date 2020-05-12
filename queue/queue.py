"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
"""


# class Queue:
#     def __init__(self):
#         self.size = 0
#         self.storage = []

#     def __len__(self):
#         return (len(self.storage))

#     def enqueue(self, value):
#         self.size += 1
#         self.storage.append(value)

#     def dequeue(self):
#         if self.size > 0:
#             self.size -= 1
#             return self.storage.pop(0)

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class Queue:
    def __init__(self, node=None):
        self.length = 0
        self.head = node
        self.tail = node

    def __len__(self):
        return self.length

    def enqueue(self, value):
        self.length += 1
        new_node = Node(value)
        if self.head:
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.head = new_node
            self.tail = new_node

    def dequeue(self):
        if self.head:
            if self.head == self.tail:
                current_tail = self.tail
                self.length -= 1
                self.head = None
                self.tail = None
                return current_tail.value

            else:
                self.length -= 1
                current = self.head
                self.head = self.head.next
                return current.value
