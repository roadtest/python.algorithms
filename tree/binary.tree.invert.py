#!/usr/bin/env python
# -*- coding: utf-8 -*-

class TreeNode: 
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

def invertTree(node):
    if node is None: 
        return None

    node.left, node.right = node.right, node.left
    invertTree(node.left)
    invertTree(node.right)
    return node

def printTree(root):
    print(root.val)
    if root.left:
        printTree(root.left)
    if root.right: 
        printTree(root.right)

sample_tree = TreeNode(1)
sample_tree.left = TreeNode(2)
sample_tree.right = TreeNode(3)
sample_tree.left.left = TreeNode(4)
sample_tree.left.right = TreeNode(5)
sample_tree.right.left = TreeNode(6)
sample_tree.right.right = TreeNode(7)

inverted_tree = invertTree(sample_tree)

printTree(inverted_tree)
