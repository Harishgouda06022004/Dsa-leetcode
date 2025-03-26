class Solution:
    def minMoves(self, nums: List[int]) -> int:
        min_nums=min(nums)
        return sum(num-min_nums for num in nums)