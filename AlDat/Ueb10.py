
# Python3 program to find the diameter of a binary tree
# A binary tree Node
class Node:
 
    # Constructor to create a new Node
    def __init__(self, data):
        self.data = data
        self.left = self.right = None
 
# utility class to pass height object
 
class Height:
    def __init(self):
        self.h = 0
 
# Optimised recursive function to find diameter
# of binary tree
 
 
def diameterOpt(root, height):
 
    # to store height of left and right subtree
    lh = Height()
    rh = Height()
 
    # base condition- when binary tree is empty
    if root is None:
        height.h = 0
        return 0
 
     
    # ldiameter --> diameter of left subtree
    # rdiameter  --> diameter of right subtree
     
    # height of left subtree and right subtree is obtained from lh and rh
    # and returned value of function is stored in ldiameter and rdiameter
     
    ldiameter = diameterOpt(root.left, lh)
    rdiameter = diameterOpt(root.right, rh)
 
    # height of tree will be max of left subtree
    # height and right subtree height plus1
 
    height.h = max(lh.h, rh.h) + 1
 
    # return maximum of the following
    # 1)left diameter
    # 2)right diameter
    # 3)left height + right height + 1
    return max(lh.h + rh.h, max(ldiameter, rdiameter))
 
# function to calculate diameter of binary tree
def diameter(root):
    height = Height()
    return diameterOpt(root, height)
 
 
# Driver Code
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.left.left = Node(6)
root.left.right.right = Node(9)
 
"""
Constructed binary tree is
            1
          /   \
        2      3
      /  \
    4     5
"""
 
# Function Call
print(diameter(root))
 
# This code is contributed by Shweta Singh(shweta44)