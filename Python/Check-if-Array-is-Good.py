1class Solution:
2    def isGood(self, nums: List[int]) -> bool:
3        n = max(nums)
4        expected = list(range(1, n + 1))
5        expected.append(n)
6        return sorted(nums) == expected