from typing import List

class Solution:
    
    def split_array(self, nums: List[int], m: int) -> int:
        l = max(nums)
        r = sum(nums)
        res = r
        
        while l <= r:
            mid = l + ((r - l) // 2)
            if self.can_split(nums, m, mid):
                res = mid
                r = mid - 1
            else:
                l = mid + 1
                
        return res
    
    def can_split(self, nums: List[int], m: int, target: int):
        subarrays = 0
        cur_sum = 0
        
        for n in nums:
            cur_sum += n
            if cur_sum > target:
                subarrays += 1
                cur_sum = n
        return subarrays + 1 <= m

