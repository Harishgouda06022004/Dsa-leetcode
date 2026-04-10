1class Solution:
2    def minimumDistance(self, nums: List[int]) -> int:
3        n = len(nums)
4        ans = float('inf')
5        for i in range(n):
6            for j in range(i+1, n):
7                for k in range(j+1, n):
8                    
9                    # check condition
10                    if nums[i] == nums[j] == nums[k]:
11                        
12                        distance = abs(i - j) + abs(j - k) + abs(k - i)
13                        ans = min(ans, distance)
14        
15        return ans if ans != float('inf') else -1