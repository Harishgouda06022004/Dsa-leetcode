1class Solution:
2    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
3        min_dist = float('inf')
4        for i in range(len(nums)):
5            if nums[i]==target:
6                min_dist = min(min_dist, abs(i - start))
7        return min_dist
8            
9