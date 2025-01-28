class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle=[]
        for row_num in range(numRows):
            row=[1]
            print(row)
            if row_num>0:
                for j in range(1,row_num):
                    row.append(triangle[row_num-1][j-1]+triangle[row_num-1][j])
                row.append(1)
            triangle.append(row)
        return triangle


