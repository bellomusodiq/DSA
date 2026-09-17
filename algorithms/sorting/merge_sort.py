class Solution:
    
    def merge_sort(self, arr: list) -> list:
        n = len(arr)
        
        if n <= 1:
            return arr
        
        m = n // 2
        
        L = arr[:m]
        R = arr[m:]
        
        L = self.merge_sort(L)
        R = self.merge_sort(R)
        
        i, l, r = 0, 0, 0
        len_l, len_r = len(L), len(R)
        sorted_array = [0] * (len_l + len_r)
        
        while l < len_l and r < len_r:
            if L[l] < R[r]:
                sorted_array[i] = L[l]
                l += 1
            else:
                sorted_array[i] = R[r]
                r += 1
            i += 1
        
        if l < len_l:
            for j in range(l, len_l):
                sorted_array[i] = L[j]
                i += 1
        
        if r < len_r:
            for j in range(r, len_r):
                sorted_array[i] = R[j]
                i += 1
                
        return sorted_array
    