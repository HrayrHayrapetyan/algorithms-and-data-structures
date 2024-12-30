class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max=-100000
        curr=0
        for i in nums:
            curr+=i
            if curr>max:
                max=curr
            if curr<0:
                curr=0
        return max
