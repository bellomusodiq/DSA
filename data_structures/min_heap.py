from typing import List, Optional

class MinHeap:
    
    def __init__(self):
        self.heap = []
        
    def insert(self, value: int) -> None:
        self.heap.append(value)
        
        self._up_heapify(len(self.heap) - 1)
        
    def _up_heapify(self, index: int) -> None:
        
        while index > 0:
            parent_index = (index - 1) // 2
            if self.heap[index] > self.heap[parent_index]:
                break
            
            self.heap[index], self.heap[parent_index] = (
                self.heap[parent_index], self.heap[index]
            )
            
            index = parent_index
            
    def pop(self) -> Optional[int]:
        if len(self.heap) == 0:
            return
        
        first_item = self.heap[0]
        last_item = self.heap.pop()
        
        if len(self.heap) == 0:
            return first_item
        
        self.heap[0] = last_item   
        self._down_heapify(0)
        
        return first_item
    
    def _down_heapify(self, index: int) -> None:
        size = len(self.heap)
        
        while True:
            left_index = (index * 2) + 1
            right_index = (index * 2) + 2
            
            smallest_index = index
            
            if (
                left_index < size and self.heap[left_index] < self.heap[smallest_index]
            ):
                smallest_index = left_index
                
            if (
                right_index < size and self.heap[right_index] < self.heap[smallest_index]
            ):
                smallest_index = right_index
                
            if smallest_index == index:
                break
            
            self.heap[index], self.heap[smallest_index] = (
                self.heap[smallest_index], self.heap[index]
            )
            
            index = smallest_index
    
    
if __name__ == "__main__":
    min_heap = MinHeap()
    for num in [10, 8, 6, 9, 2]:
        min_heap.insert(num)
        print(min_heap.heap)
        
    for _ in range(3):
        print(min_heap.pop(), min_heap.heap)