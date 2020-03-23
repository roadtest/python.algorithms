#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Node():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

tree = None
nodes = list(map(int, input().split()))

for element in nodes:
    tree = insertNode(tree, element)
