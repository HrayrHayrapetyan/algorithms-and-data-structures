class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        di = {}
        major_key = nums[0]

        for i in nums:
            if i in di.keys():
                di[i] += 1
            else:
                di[i] = 1
        print(di)

        for i, j in di.items():
            if j > di[major_key]:
                major_key = i

        return major_key




