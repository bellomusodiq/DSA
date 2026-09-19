from data_structures.linked_list import LinkedList
from typing import Any

class Queue:
    
    def __init__(self, *args, capacity: int = None):
        self.capacity = capacity
        self.list = LinkedList(*args)
        
    @property
    def can_enqueue(self):
        if self.capacity is None:
            return True
        return self.list.length < self.capacity
    
    @property
    def can_dequeue(self):
        return self.list.length > 0
        
    def enqueue(self, value: Any) -> None:
        if self.can_enqueue:
            self.list.append(value)
    
    def pop(self) -> Any:
        if not self.can_dequeue:
            return None
        item = self.list.head
        self.list.head = self.list.head.next
        self.list.length -= 1
        
        if self.list.length == 0:
            self.list.tail = None
        return item.value
    
    def peek(self) -> Any:
        if not self.can_dequeue:
            return None
        item = self.list.head
        return item.value