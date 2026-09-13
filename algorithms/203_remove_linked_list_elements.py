from data_structures.linked_list import LinkedListNode

class Solution:
    
    def removeElements(self, head: LinkedListNode, value: int) -> LinkedListNode:
        dummy = LinkedListNode(next_node=head)
        
        prev, curr = dummy, dummy.next
        
        while curr:
            nxt = curr.next
            
            if curr.value == value:
                prev.next = nxt
            else:
                prev = curr
            curr = nxt
        
        return dummy.next