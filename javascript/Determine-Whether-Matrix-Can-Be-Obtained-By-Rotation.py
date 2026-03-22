1class Solution:
2    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
3        def rotate(matrix):
4            n=len(matrix)
5            for i in range(n):
6                for j in range(i+1,n):
7                    matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
8            for row in matrix:
9                row.reverse()
10            return matrix
11        for i in range(4):
12            if rotate(mat)==target:
13                return True
14        return False