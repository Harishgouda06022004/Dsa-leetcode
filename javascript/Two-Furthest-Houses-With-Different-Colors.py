1class Solution:
2    def maxDistance(self, colors: List[int]) -> int:
3        n=len(colors)
4        max_dist=0
5        for i in range(n):
6            if colors[i]!=colors[0]:
7                max_dist=max(max_dist,i)
8            if colors[i]!=colors[n-1]:
9                max_dist=max(max_dist,n-1-i)
10        return max_dist