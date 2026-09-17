class Solution:
    
    def quick_sort(self, arr: list) -> list:
        n = len(arr)
        
        if n <= 1:
            return arr
        
        p = arr[-1]
        L, R = [], []
        for p_index in range(0, n - 1):
            if arr[p_index] <= p:
                L.append(arr[p_index])
            else:
                R.append(arr[p_index])
                
        L = self.quick_sort(L)
        R = self.quick_sort(R)
        
        return L + [p] + R
    