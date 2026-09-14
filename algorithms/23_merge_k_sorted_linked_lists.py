from data_structures.linked_list import LinkedListNode


class Solution:

    def mergeKLists(self, lists: list[LinkedListNode]) -> LinkedListNode:
        if not lists:
            return None
        
        while len(lists) > 1:
            merged_lists = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if i + 1 < len(lists) else None
                merged_lists.append(self.mergeLists(l1, l2))
            lists = merged_lists
        return lists[0]
    
    def mergeLists(self, l1: LinkedListNode, l2: LinkedListNode) -> LinkedListNode:
        dummy = LinkedListNode()
        tail = dummy
        
        while l1 and l2:
            if l1.value <= l2.value:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
            
        tail.next = l1 or l2
        
        return dummy.next
        