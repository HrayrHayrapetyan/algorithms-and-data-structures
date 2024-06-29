class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        di={}

        for i in nums:
            if i in di.keys():
                di[i]+=1
            else:
                di[i]=1

        for i in di.values():
            if i>=2:
                return True
        return False