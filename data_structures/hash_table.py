try:
    from data_structures.linked_list import LinkedListNode
except ModuleNotFoundError:
    from linked_list import LinkedListNode
from typing import Any, List, Optional, Tuple

class KeyValue:
    def __init__(self, key: str, value: Any) -> None:
        self.key = key
        self.value = value

class HashTable:
    
    def __init__(self, data: Optional[List[Tuple[str, Any]]] = None, max_size: int = 256) -> None:
        self.max_size = max_size
        self.array = [None for _ in range(max_size)]
        self.len = 0
        if data:
            for key, value in data:
                self.set(key, value)
        
    def get_hash_key(self, key: str) -> int:
        h = 0
        for char in key:
            h += ord(char)
        return h % self.max_size
    
    def set(self, key: str, value: Any):
        hash_key = self.get_hash_key(key)
        if self.update_collision_table(hash_key, key, value):
            self.len += 1
        
    def get(self, key: str) -> Any:
        hash_key = self.get_hash_key(key)
        item = self.array[hash_key]

        while item:
            if item.value.key == key:
                return item.value.value
            item = item.next
        return None
        
    def delete(self, key: str) -> None:
        hash_key = self.get_hash_key(key)
        if self.delete_from_collision_table(hash_key, key):
            self.len -= 1
        
    def has_key(self, key) -> bool:
        hash_key = self.get_hash_key(key)
        item = self.array[hash_key]

        while item:
            if item.value.key == key:
                return True
            item = item.next
        return False
        
    def update_collision_table(self, hash_key: int, key: str, value: Any) -> bool:
        item = self.array[hash_key]
        if item is None:
            self.array[hash_key] = LinkedListNode(KeyValue(key, value))
            return True

        while item:
            if item.value.key == key:
                item.value.value = value
                return False
            if item.next is None:
                item.next = LinkedListNode(KeyValue(key, value))
                return True
            item = item.next
            
    def delete_from_collision_table(self, hash_key: int, key: str) -> bool:
        item = self.array[hash_key]
        prev = None
        while item:
            if item.value.key == key:
                if prev is None:
                    self.array[hash_key] = item.next
                else:
                    prev.next = item.next
                return True
            prev = item
            item = item.next
        return False
        
    def __getitem__(self, key: str) -> Any:
        return self.get(key)
        
    def __setitem__(self, key: str, value: Any) -> None:
        self.set(key, value)
    
    def __contains__(self, key: str) -> str:
        return self.has_key(key)
    
    def __delitem__(self, key):
        self.delete(key)
        

if __name__ == "__main__":
    hash_table = HashTable(
        [("first", 1), ("second", 2), ("third", 3)]
    )
    print(hash_table["first"])
