class Solution:
    
    def is_perfect_square(self, num: int) -> int:
        l, r = 1, num
        
        while l <= r:
            mid = l + ((r - l) // 2)
            if mid * mid < num:
                l = mid + 1
            elif mid * mid > num:
                r = mid - 1
            else:
                return True
        return False
    
    