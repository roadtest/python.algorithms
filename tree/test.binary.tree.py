#!/usr/bin/env python
class Node:
    """A simple Binary Node to be used in a Tree"""

    def __init__(self, value=-1, leftNode=None, rightNode=None):
        self.value = value
        self.leftNode = leftNode
        self.rightNode = rightNode

class BinaryTree:
    def __init__(self, root=None):
        self.root = root
        self.noOfLeftNodes = 0
        self.noOfRightNodes = 0

    def addNode(self, root, node):
        if self.root is None:
            self.root = node
            return
        if root.leftNode is None:
            root.leftNode = node
            self.noOfLeftNodes += 1
            return
        elif root.rightNode is None:
            root.rightNode = node
            self.noOfRightNodes += 1
            return

        else:
            if self.noOfLeftNodes - self.noOfRightNodes < 2:
                self.addNode(root.leftNode, node)
            else:
                self.addNode(root.rightNode, node)

    def preorder(self, root):
        if root is None:
            return
        print(root.value)
        self.preorder(root.leftNode)
        self.preorder(root.rightNode)

    #Test stub
bt = BinaryTree()
nodes = [1, 2, 3, 4, 5, 6, 7]
for i in range(len(nodes)):
    bt.addNode(bt.root, Node(nodes[i]))
print('---Binary Tee---')
bt.preorder(bt.root)
