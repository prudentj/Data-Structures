"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # If it is greater than or equal to add it to the right
        # If there is a node there pass the value it it
        # Else make a node
        if value >= self.value:
            if self.right:
                self.right.insert(value)
            else:
                self.right = BinarySearchTree(value)
        # Less than add it to the left
        # If there is a node there pass the value it it
        # Else make a node
        else:
            if self.left:
                self.left.insert(value)
            else:
                self.left = BinarySearchTree(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # This is the value we seek
        if self.value == target:
            return True
        # If the value we want is here it is to the right
        elif target > self.value:
            if self.right:
                self.right.contains(target)
            else:
                # It does not exist
                return False
        # If the value we want is here it is to the left
        elif target < self.value:
            if self.left:
                self.left.contains(target)
            else:
                # It does not exist
                return False

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right:
            self.right.get_max()
        else:
            return self.value

    # Call the function `fn` on the value of each node
    # If left or right exist call that function
    def for_each(self, fn):
        fn(self.value)
        if(self.right):
            self.right.for_each(fn)
        if(self.left):
            self.left.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal

    def in_order_print(self, node):
        # if self.left:
        #     self.left.in_order_print(node)
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
