class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        def check(x):
            rotation_top=0
            rotation_bottom=0
            for i in range(len(tops)):
                if tops[i]!=x and bottoms[i]!=x:
                    return -1
                elif tops[i]!=x:
                    rotation_top+=1
                elif bottoms[i]!=x:
                    rotation_bottom+=1
            return min(rotation_top,rotation_bottom)
        result=check(tops[0])
        if result!=-1:
            return result
        return check(bottoms[0])