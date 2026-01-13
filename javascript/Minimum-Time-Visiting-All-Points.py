1class Solution:
2    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
3        ans=0
4        for i  in range(1,len(points)):
5            ans+=max(abs(points[i][0]-points[i-1][0]),abs(points[i][1]-points[i-1][1]))
6        return ans