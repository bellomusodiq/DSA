
class ListNode:
    
    def __init__(self, key=None):
        self.key = key
        self.next = None
        
class MyHashSet:
    
    def __init__(self):
        self.set = [ListNode() for _ in range(10**4)]
        
    def get_hash(self, key: int) -> int:
        return key % len(self.set)
    
    def add(self, key: int) -> None:
        hash_key = self.get_hash(key)
        curr = self.set[hash_key]
        while curr.next:
            if curr.next.key == key:
                return
            curr = curr.next
        curr.next = ListNode(key=key)
    
    def remove(self, key: int) -> None:
        hash_key = self.get_hash(key)
        curr = self.set[hash_key]
        while curr.next:
            if curr.next.key == key:
                curr.next = curr.next.next
                return
            curr = curr.next
    
    def contains(self, key: int) -> bool:
        hash_key = self.get_hash(key)
        curr = self.set[hash_key]
        while curr.next:
            if curr.next.key == key:
                return True
            
            curr = curr.next
        return False