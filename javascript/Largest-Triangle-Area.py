class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        n=len(points)
        area=0
        for i in range(n-2):
            x1,y1=points[i]
            for j in range(n-1):
                x2,y2=points[j]
                for k in range(n):
                    x3,y3=points[k]
                    if abs(0.5*(x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2)))>area:
                        area=abs(0.5*(x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2)))
        return area