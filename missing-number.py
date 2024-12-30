class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        for i in range(0, len(nums) + 1):
            chlp = False
            for j in nums:
                if i == j:
                    chlp = True
            if not chlp:
                return i

