class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        l = len(nums1) - 1
        while (n):
            if not m:
                for i in range(0, n):
                    nums1[i] = nums2[i]
                return nums1
            if nums1[m - 1] < nums2[n - 1]:
                nums1[l] = nums2[n - 1]
                n -= 1
                l -= 1
            else:
                nums1[m - 1], nums1[l] = nums1[l], nums1[m - 1]
                m -= 1
                l -= 1

