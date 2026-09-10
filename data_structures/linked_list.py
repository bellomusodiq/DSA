

class LinkedListNode:

    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next = next_node
        
        
class LinkedList:
    
    def __init__(self, *args):
        self.head = None
        self.length = 0
        
        previous_node = None
        for item in args:
            node = LinkedListNode(value=item)
            if previous_node is None:
                self.head = node
            else:
                previous_node.next = node
            previous_node = node
            self.length += 1
            
    def insert(self, value, position=None):
        if position == 0:
            self.prepend(value)
            return
        
        if position is None:
            position = self.length
        
        if not 0 <= position <= self.length:
            raise IndexError("insert position is out of range")
        
        node = self.head
        for _ in range(1, position):
            node = node.next
           
        new_node = LinkedListNode(value, node.next)
        node.next = new_node
        self.length += 1
        
    def get(self, position):
        
        if not 0 <= position < self.length:
            raise IndexError("get index is out of range")

        node = self.head
        for _ in range(position):
            node = node.next
        return node.value
    
    def prepend(self, value):
        self.head = LinkedListNode(value, next_node=self.head)
        self.length += 1
        
    def delete(self, position):
        
        if not 0 <= position < self.length:
            raise IndexError("delete index is out of range")
        
        if position == 0:
            self.head = self.head.next
        else:
            node = self.head
            for _ in range(1, position):
                node = node.next
               
            node.next = node.next.next
            
        self.length -= 1
            
            
    def __str__(self):
        item_list = []
        node = self.head
        while node:
            item_list.append(str(node.value))
            node = node.next
        return " -> ".join(item_list)
            
            