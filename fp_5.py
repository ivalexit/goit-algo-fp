import matplotlib.pyplot as plt
import networkx as nx
from queue import Queue
from collections import deque

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def insert(root, value):
    if root is None:
        return TreeNode(value)
    queue = Queue()
    queue.put(root)
    while not queue.empty():
        temp = queue.get()
        if not temp.left:
            temp.left = TreeNode(value)
            break
        else:
            queue.put(temp.left)
        if not temp.right:
            temp.right = TreeNode(value)
            break
        else:
            queue.put(temp.right)
    return root