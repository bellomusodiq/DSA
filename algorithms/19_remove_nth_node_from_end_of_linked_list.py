from data_structures.linked_list import LinkedListNode

class Solution:
    
    def removeNthFromEnd(self, list: LinkedListNode, n: int) -> LinkedListNode:
        dummy = LinkedListNode(next_node=list)
        left = dummy
        right = list
        
        while right and n > 0:
            right = right.next
            n -= 1
            
        while right:
            right = right.next
            left = left.next
            
        left.next = left.next.next            
        return dummy.next