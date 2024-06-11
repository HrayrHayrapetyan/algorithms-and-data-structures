class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        major_index=0
        for i in range(0,len(nums)-1):
            count=0
            for j in range(i+1,len(nums)):
                if nums[i]==nums[j]:
                    count+=1
            if count>=len(nums)/2:
                major_index=i
        return nums[major_index]
