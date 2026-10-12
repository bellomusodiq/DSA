from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        counts, prefix_sum = 0, 0
        prefix_sums = {0: 1}
        
        for num in nums:
            prefix_sum += num
            diff = prefix_sum - k
            counts += prefix_sums.get(diff, 0)
            prefix_sums[prefix_sum] = 1 + prefix_sums.get(prefix_sum, 0)
            
        return counts