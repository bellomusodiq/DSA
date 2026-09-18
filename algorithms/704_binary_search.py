class Solution:
    
    def binary_search(self, arr: list, target: int) -> int:
        l, r = 0, len(arr) - 1
        
        while l <= r:
            m = l + ((r - l) // 2)
            if arr[m] > target:
                r = m - 1
            elif arr[m] < target:
                l = m + 1
            else:
                return m
        return -1
    
