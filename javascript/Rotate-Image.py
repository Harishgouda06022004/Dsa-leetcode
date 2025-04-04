class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # result=[list(col)[::-1] for col in zip(*matrix)]
        # print(result)
        # return result
        n=len(matrix)
        for i in range(n):
            for j in range(i,n):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        for row in matrix:
            row.reverse()
        return matrix