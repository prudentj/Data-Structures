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

# Coded for as an Array

# class Queue:
#     def __init__(self):
#         self.size = 0
#         self.storage = []

# returns the length of storage

#     def __len__(self):
#         return (len(self.storage))

# Adds a value to the end of storage

#     def enqueue(self, value):
#         self.size += 1
#         self.storage.append(value)

# Remove and return the first element from the front of the Array

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
    # returns the length stored in the constuctor

    def __len__(self):
        return self.length
    # adds a node to the queue with a input Value

    def enqueue(self, value):
        self.length += 1
        new_node = Node(value)
        # If there already something in the queue add a node
        if self.head:
            self.tail.next = new_node
            self.tail = new_node
        # If the Queue is empty add a node
        else:
            self.head = new_node
            self.tail = new_node

    def dequeue(self):
        # If something is in the queue
        if self.head:
            # If there is only one item in the queue, return and remove it
            # Set head and tail to none
            if self.head == self.tail:
                current_tail = self.tail
                self.length -= 1
                self.head = None
                self.tail = None
                return current_tail.value
            # If there is more than one item in the queue return and remove it from head
            # make the new first item the head
            else:
                self.length -= 1
                current = self.head
                self.head = self.head.next
                return current.value
