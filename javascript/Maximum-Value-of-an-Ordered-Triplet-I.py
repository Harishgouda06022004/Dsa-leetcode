1class Solution:
2    def maximumTripletValue(self, nums: List[int]) -> int:
3        max_value=0
4        n=len(nums)
5        for i in range(n):
6            for j in range(i+1,n):
7                for k in range(j+1,n):
8                    current_value=(nums[i] - nums[j]) * nums[k]
9                    if current_value>max_value:
10                       max_value=current_value
11        return max_value if max_value>0 else 0