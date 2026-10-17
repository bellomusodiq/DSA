from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_p = min_p = nums[0]
        maximum_product = max_p
        
        for num in nums[1:]:
            temp_min_p = min_p
            min_p = min(num, min_p * num, max_p * num)
            max_p = max(num, temp_min_p * num, max_p * num)
            maximum_product = max(maximum_product, max_p)
            
        return maximum_product