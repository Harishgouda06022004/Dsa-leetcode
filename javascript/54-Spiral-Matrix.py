class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top=0
        bottom=len(matrix)-1
        left=0
        right=len(matrix[0])-1
        spiral=[]
        while top<=bottom and left<=right:
            for i in range(left,right+1):
                spiral.append(matrix[top][i])
            top+=1
            for j in range(top,bottom+1):
                spiral.append(matrix[j][right])
            right-=1
            if top<=bottom:
                for k in range(right,left-1,-1):
                    spiral.append(matrix[bottom][k])
                bottom-=1
            if left<=right:
                for l in range(bottom,top-1,-1):
                    spiral.append(matrix[l][left])
                left+=1
        return spiral