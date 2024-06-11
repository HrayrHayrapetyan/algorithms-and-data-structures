class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        output=[]
        for i in nums1:
            for j in nums2:
                if i==j:
                    repeats=False
                    for k in output:
                        if i==k:
                            repeats=True
                            break
                    if not repeats:
                        output.append(i)
        return output
