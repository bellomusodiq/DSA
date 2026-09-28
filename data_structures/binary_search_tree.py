from typing import Any, List


class Node:
    def __init__(self, value: int = None, left: Any = None, right: Any = None):
        self.value = value
        self.left: "Node" = left
        self.right: "Node" = right
        

class BinarySearchTree:
    
    def __init__(self):
        
        self.root = None
        self.len = 0
        
    def insert(self, value: int) -> None:
        if self.root is None:
            self.root = Node(value=value)
            self.len += 1
            return
        
        current = self.root
        
        while True:
            if value < current.value:
                if current.left is None:
                    current.left = Node(value=value)
                    self.len += 1
                    return
                current = current.left
            elif value > current.value:
                if current.right is None:
                    current.right = Node(value=value)
                    self.len += 1
                    return
                current = current.right
            else:
                return # prevent duplicate
            
    def search(self, value: int) -> None:
        current = self.root
        
        while current is not None:
            if value == current.value:
                return True
        
            if value < current.value:
                current = current.left
            if value > current.value:
                current = current.right        
        return False
    
    def inorder(self):
        values = []
        self._inorder(self.root, values)
        return values
    
    def _inorder(self, node: Node, values: List[int]):
        if node is None:
            return
        self._inorder(node.left, values)
        values.append(node.value)
        self._inorder(node.right, values)
        
    def preorder(self):
        values = []
        self._preorder(self.root, values)
        return values
    
    def _preorder(self, node: Node, values: List[int]):
        if node is None:
            return
        
        values.append(node.value)
        self._preorder(node.left, values)
        self._preorder(node.right, values)
        
    def postorder(self):
        values = []
        self._postorder(self.root, values)
        
        return values
    
    def _postorder(self, node: Node, values: List[int]):
        if node is None:
            return
        
        self._postorder(node.left, values)
        self._postorder(node.right, values)
        values.append(node.value)
    
    def __len__(self):
        return self.len
