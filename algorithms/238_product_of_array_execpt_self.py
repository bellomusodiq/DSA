from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> int:
        answers = [0] * len(nums)
        prefix = 1
        for i in range(len(nums)):
            answers[i] = prefix
            prefix *= nums[i]
            
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            answers[i] *= postfix
            postfix *= nums[i]
            
        return answers