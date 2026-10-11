from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for _ in range(len(nums) + 1)]
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        for key, value in count.items():
            freq[value].append(key)
            
        res = []
        for i in range(len(nums), -1, -1):
            for el in freq[i]:
                res.append(el)
                if len(res) == k:
                    return res