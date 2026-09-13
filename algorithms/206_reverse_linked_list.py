from data_structures.linked_list import LinkedListNode

class Solution:
    
    def reverseList(self, head: LinkedListNode) -> LinkedListNode:
        if not (head and head.next):
            return head
        
        prev = None
        current = head
        while current:
            temp = current.next
            current.next = prev
            prev, current = current, temp
            
        return prev
    
    def reverseListReccursive(self, head: LinkedListNode) -> LinkedListNode:
        if not (head and head.next):
            return next
        
        new_head = self.reverseListReccursive(head.next)
        
        head.next.next = head
        head.next = None
        
        return new_head
        