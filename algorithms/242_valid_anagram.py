class Solution:
    
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hashset = [0] * 26
        for i in range(len(s)):
            hashset[ord(s[i]) - ord("a")] += 1
            hashset[ord(t[i]) - ord("a")] -= 1
            
        for num in hashset:
            if num != 0:
                return False
        return True