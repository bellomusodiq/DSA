class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        if len(nums) <= 1:
            return nums
        m = len(nums) // 2
        L = nums[:m]
        R = nums[m:]
        L = self.sortArray(L)
        R = self.sortArray(R)

        l, r = 0, 0
        merged_array = []
        while l < len(L) and r < len(R):
            if L[l] <= R[r]:
                merged_array.append(L[l])
                l += 1
            else:
                merged_array.append(R[r])
                r += 1

        if l < len(L):
            merged_array.extend(L[l:])
        if r < len(R):
            merged_array.extend(R[r:])

        return merged_array