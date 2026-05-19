1class Solution:
2    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
3        s=set(nums1)
4        for num in nums2:
5            if num in s:
6                return num
7        return -1