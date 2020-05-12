"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
   How it is stored in mememory. It is also easier to add additional attributes
"""

# This one uses an array
# class Stack:
#     def __init__(self):
#         self.size = 0
#         self.storage = []

#     def __len__(self):
#         return(len(self.storage))

#     def push(self, value):
#         self.storage.append(value)

#     def pop(self):
#         if len(self.storage) > 0:
#             return self.storage.pop()
#         return None

# This one uses a linked list


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class Stack:
    def __init__(self, node=None):
        self.length = 0
        self.head = node
        self.tail = node

    def __len__(self):
        return self.length

    def push(self, value):
        self.length += 1
        new_node = Node(value)
        if self.head:
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.head = new_node
            self.tail = new_node

    def pop(self):
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
                last = self.tail
                while current.next != last:
                    current = current.next
                current.next = None
                self.tail = current
                return last.value
