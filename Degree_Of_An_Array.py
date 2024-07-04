class Solution:
    def findShortestSubArray(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return 1
        elif nums is None:
            return 0
        di = {}
        for i in nums:
            if i in di.keys():
                di[i] += 1
            else:
                di[i] = 1
        degree = max(di.values())
        if degree == 1:
            return 1
        lengths = []
        max_keys = []
        for i, j in di.items():
            if j == degree:
                max_keys.append(i)

        lengths = []
        for i in range(len(nums)):
            if nums[i] in max_keys:
                j = len(nums) - 1
                while nums[i] != nums[j] and i < j:
                    j -= 1
                if i >= j:
                    break
                length = j - i + 1
                lengths.append(length)
                max_keys.remove(nums[i])

        return min(lengths)


















