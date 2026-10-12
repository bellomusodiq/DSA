from typing import List

class Solution:
    
    def __init__(self, nums: List[int]) -> None:
        self.prefix_sums = []
        prefix_sum = 0
        for num in nums:
            prefix_sum += num
            self.prefix_sums.append(prefix_sum)
            
    def sumRange(self, left: int, right: int) -> int:
        left_value = 0
        if left != 0:
            left_value = self.prefix_sums[left - 1]
        return self.prefix_sums[right] - left_value