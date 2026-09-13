from data_structures.linked_list import LinkedListNode

class Solution:
    
    def isPanlindrome(self, head: LinkedListNode) -> bool:
        if not head:
            return False
        
        if not head.next:
            return True
        
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        prev = None
        second = slow.next
        slow.next = None
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
            
        # compare
        second = prev
        first = head
        while second:
            if first.value != second.value:
                return False
            first = first.next
            second = second.next
        return True
