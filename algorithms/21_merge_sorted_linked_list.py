from data_structures.linked_list import LinkedListNode


class Solution:

    def mergeSortedList(self, l1: LinkedListNode, l2: LinkedListNode) -> LinkedListNode:
        dummy = LinkedListNode()

        current = dummy
        while l1 and l2:
            if l1.value <= l2.value:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next

        current.next = l1 or l2
        return dummy.next