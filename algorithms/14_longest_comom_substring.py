from typing import List

class Solution:
    
    def longestComonSubstring(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        
        for i, c in enumerate(strs[0]):
            for str_ in strs[1:]:
                if len(str_) == i or str_[i] != c:
                    return str_[:i]
                
        return strs[0]
