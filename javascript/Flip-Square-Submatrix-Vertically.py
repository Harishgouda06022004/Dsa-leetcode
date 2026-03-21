1class Solution:
2    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
3        top=x
4        bottom=x+k-1
5        while top<bottom:
6            for j in range(y,y+k):
7                grid[top][j],grid[bottom][j]=grid[bottom][j],grid[top][j]
8            top+=1
9            bottom-=1
10        return grid