1class Solution:
2    def search(self, nums: List[int], target: int) -> int:
3        for i in range(0,len(nums)):
4            if nums[i]==target:
5                return i
6        return -1