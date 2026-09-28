from typing import Any, List, Optional


class Node:
    def __init__(self, value: int = None, left: Any = None, right: Any = None):
        self.value = value
        self.left: "Node" = left
        self.right: "Node" = right
        

class BinarySearchTree:
    
    def __init__(self):
        self.root = None
        
    def insert(self, value: int) -> None:
        if self.root is None:
            self.root = Node(value=value)
            return
        
        current = self.root
        
        while True:
            if value < current.value:
                if current.left is None:
                    current.left = Node(value=value)
                    return
                current = current.left
            elif value > current.value:
                if current.right is None:
                    current.right = Node(value=value)
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
        
    def min(self, node: Optional[Node] = None) -> Optional[int]:
        current = node if node is not None else self.root
        
        if current is None:
            return
        
        while current.left:
            current = current.left
            
        return current.value
    
    def max(self, node: Optional[Node] = None) -> Optional[int]:
        current = node if node is not None else self.root 
        if current is None:
            return
        
        while current.right:
            current = current.right
            
        return current.value
    
    def delete(self, value: int) -> None:
        self.root = self._delete(self.root, value)
        
    def _delete(self, node: Node, value: int) -> Optional[Node]:
        if node is None:
            return None
        
        if value < node.value:
            node.left = self._delete(node.left, value)
            
        elif value > node.value:
            node.right = self._delete(node.right, value)
            
        else:
            # Case 1: No right child
            if node.right is None:
                return node.left
            
            # Case 2: No left child
            if node.left is None:
                return node.right
            # Case 3: Both children
            successor = self.min(node.right)
            
            node.value = successor
            
            node.right = self._delete(node.right, successor)
            
        return node
        