1class Solution:
2    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
3        n = len(nums)
4        ans = 0
5
6        for i in range(n):
7            balance = 0
8            for j in range(i, n):
9                if nums[j] == target:
10                    balance += 1
11                else:
12                    balance -= 1
13
14                if balance > 0:
15                    ans += 1
16
17        return ans