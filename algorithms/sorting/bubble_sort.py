
class Solution:
    
    def bubble_sort(self, arr: list) -> list:
        n = len(arr)
        
        for i in range(n):
            swapped = False
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    swapped = True
            if not swapped:
                break
            
        return arr
    
    def bubble_sort_recursive(self, arr: list, n: int = None) -> list:
        if not n:
            n = len(arr)
        
        if n <= 1:
            return arr
        
        swapped = False
        for i in range(n - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
        
        if not swapped:
            return arr
        
        return self.bubble_sort_recursive(arr, n - 2)
    