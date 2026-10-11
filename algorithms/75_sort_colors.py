from typing import List

class Solution:
    
    def sortColors(self, nums: List[int]) -> None:
        bucket = {0: 0, 1: 0, 2: 0}
        
        for num in nums:
            bucket[num] += 1
            
        index = 0
        for key in [0, 1, 2]:
            for _ in range(bucket[key]):
                nums[index] = key
                index += 1