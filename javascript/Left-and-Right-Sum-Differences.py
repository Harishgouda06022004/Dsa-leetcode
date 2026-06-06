1class Solution:
2    def leftRightDifference(self, nums: List[int]) -> List[int]:
3        n=len(nums)
4        answer=[]
5        for i in range(n):
6            leftSum=0
7            RightSum=0
8            for j in range(i):
9                leftSum+=nums[j]
10            for j in range(i+1,n):
11                RightSum+=nums[j]
12            answer.append(abs(leftSum-RightSum))
13        return answer