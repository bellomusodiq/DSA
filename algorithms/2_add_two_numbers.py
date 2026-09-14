from data_structures.linked_list import LinkedListNode

class Solution:
    
    def addTwoNumbers(self, l1: LinkedListNode, l2: LinkedListNode) -> LinkedListNode:
        dummy = LinkedListNode()
        tail = dummy
        
        carry = 0
        while l1 or l2 or carry:
            val1 = l1.value if l1 else 0
            val2 = l2.value if l2 else 0
            
            val = val1 + val2 + carry
            carry = val // 10
            val = val % 10
            
            tail.next = LinkedListNode(value=val)
            
            tail = tail.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        return dummy.next
            