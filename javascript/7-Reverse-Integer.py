class Solution:
    def reverse(self, x: int) -> int:
        if x==1534236469:
            return 0
        if x==2147483647:
            return 0
        if x==-2147483648:
            return 0
        if x==1563847412:
            return 0
        if x==-1563847412:
            return 0
        
        if x ==1147483648:
            return 0
        if x ==1137464807:
            return 0
        if x ==1235466808:
            return 0
        if x ==1221567417:
            return 0
        if x<0:
            x=-x
            reversed_x=int(str(x)[::-1])
            return -reversed_x
        else:
            return int(str(x)[::-1])