from typing import List

class Solution:
    
    def runningSum(self, nums: List[int]) -> List[int]:
        res = []
        
        for i in range(len(nums)):
            if i == 0:
                res.append(nums[i])
            else:
                res.append(
                    res[i - 1] + nums[i]
                )
                
        return res