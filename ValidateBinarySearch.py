#Python Program for Validation of Binary Tree
""" A binary search tree (BST) is a binary tree whose elements are positioned in a special order such that in each binary search tree all values in the left subtree are less than those in the subtree on the right.
"""

class binarytree:
    def __init__(self, val):
        self.val = val
        self.leftnode = leftnode
        self.rightnode = rightnode
import sys
class BinarySearchTree:
    def validate_BST(self, root: binarytree) -> bool:
        return self.valid(root, sys.maxsize, -sys.maxsize)
    def valid(self, root, max_, min_):
        if root == None:
            return True
        else:
            return False
        return self.valid(root.leftnode, root.val, min_) and self.valid(root.rightnode, max_, root.val)