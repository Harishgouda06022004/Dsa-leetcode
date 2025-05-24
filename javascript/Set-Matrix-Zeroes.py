class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        \\\
        Do not return anything, modify matrix in-place instead.
        \\\
        zero_pos=[]
        m,n=len(matrix),len(matrix[0])
        print(m)
        print(n)
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    zero_pos.append((i,j))
        print(zero_pos)
        def make_row_zero(row):
            for i in range(len(row)):
                row[i]=0
        def make_col_zero(matrix,col_index):
            for row in matrix:
                row[col_index]=0
        for row,col in zero_pos:
            make_row_zero(matrix[row])
            make_col_zero(matrix,col)

        