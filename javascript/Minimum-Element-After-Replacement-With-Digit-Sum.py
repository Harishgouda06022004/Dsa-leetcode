1class Solution:
2    def minElement(self, nums: List[int]) -> int:
3        mini = float('inf')
4        for n in nums:
5            digit_sum=0
6            for digit in str(n):
7                digit_sum+=int(digit)
8            mini=min(mini,digit_sum)
9        return mini