from collections import defaultdict
from typing import List

class Solution:
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = defaultdict(list)
        
        for s in strs:
            hash_ = [0] * 26
            for c in s:
                hash_[ord(c) - ord("a")] += 1
                
            hash_map[tuple(hash_)].append(s)
            
        return list(hash_map.values())