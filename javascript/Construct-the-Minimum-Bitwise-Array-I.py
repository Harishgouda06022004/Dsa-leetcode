1class Solution:
2    def minBitwiseArray(self, nums: List[int]) -> List[int]:
3        ans = []
4        for n in nums:
5            if n != 2:
6                ans.append(n - ((n + 1) & (-n - 1)) // 2)
7            else:
8                ans.append(-1)
9        return ans