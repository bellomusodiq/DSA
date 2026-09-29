from typing import List, Optional

class MaxHeap:
    
    def __init__(self):
        self.heap: List[int] = []
        
    def insert(self, value: int):
        self.heap.append(value)
        
        index = len(self.heap) - 1
        
        self._heapify_up(index)
        
    def _heapify_up(self, index):
        
        while index > 0:
            parent_index = (index - 1) // 2
            
            if self.heap[index] < self.heap[parent_index]:
                break
            
            self.heap[index], self.heap[parent_index] = (
                self.heap[parent_index], self.heap[index]
            )
            
            index = parent_index
            
    def pop(self) -> Optional[int]:
        if len(self.heap) == 0:
            return None
        
        first_item = self.heap[0]
        last_item = self.heap.pop()

        if len(self.heap) == 0:
            return first_item
        
        self.heap[0] = last_item
        
        self._heapify_down(0)
        
        return first_item
    
    def _heapify_down(self, index):
        size = len(self.heap)
        while True:
            left_index = (2 * index) + 1
            right_index = (2 * index) + 2
            
            largest_index = index
            
            if (
                left_index < size and self.heap[left_index] > self.heap[largest_index]
            ):
                largest_index = left_index
                
            if (
                right_index < size and self.heap[right_index] > self.heap[largest_index]
            ):
                largest_index = right_index
                
            if largest_index == index:
                break
            
            self.heap[index], self.heap[largest_index] = (
                self.heap[largest_index], self.heap[index]
            )
            
            index = largest_index
            
    def peak(self):
        if len(self.heap) == 0:
            return
        return self.heap[0]
    
    def __len__(self):
        return len(self.heap)
    
