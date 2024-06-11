class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        appears = False
        for i in range(0, len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    appears = True
                    break
            if appears:
                break
        return appears

