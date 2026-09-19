try:
    from data_structures.linked_list import LinkedList
except ModuleNotFoundError:
    from linked_list import LinkedList
from typing import Any, List

class Stack:
    
    def __init__(self, *args: List[Any], capacity: int = None):
        self.list = LinkedList(*args)
        self.capacity = capacity
        
    @property
    def can_push(self):
        return self.capacity is None or self.list.length < self.capacity
    
    @property
    def can_pop(self):
        return self.list.length > 0
        
    def push(self, item: Any) -> bool:
        """push method takes in an data type and push to the stack

        Args:
            item (Any): any data type that needs to be stored

        Returns:
            bool: returns True if push was successful or stack overflow (False)
        """
        if not self.can_push:
            return False
        self.list.prepend(item)
        return True
    
    def peak(self) -> bool:
        return self.list.head.value
    
    def pop(self) -> Any:
        if self.can_pop:
            head = self.list.head
            self.list.head = head.next
            self.list.length -= 1
            return head.value
        return None
    
    def __str__(self):
        return str(self.list)
    
