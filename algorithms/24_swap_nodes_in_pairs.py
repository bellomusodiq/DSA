from data_structures.linked_list import LinkedListNode

class Solution:
    
    def swapPairs(self, list: LinkedListNode) -> LinkedListNode:
        dummy = LinkedListNode(next_node=list)
        prev, current = dummy, list
        
        while current and current.next:
            next_current = current.next.next
            second = current.next
            
            second.next = current
            current.next = next_current
            prev.next = second
            
            prev = current
            current = next_current
            
        return dummy.next