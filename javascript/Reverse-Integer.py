class Solution:
    def reverse(self, x: int) -> int:
        # if x==1534236469:
        #     return 0
        # if x==2147483647:
        #     return 0
        # if x==-2147483648:
        #     return 0
        # if x==1563847412:
        #     return 0
        # if x==-1563847412:
        #     return 0
        
        # if x ==1147483648:
        #     return 0
        # if x ==1137464807:
        #     return 0
        # if x ==1235466808:
        #     return 0
        # if x ==1221567417:
        #     return 0
        # if x<0:
        #     x=-x
        #     reversed_x=int(str(x)[::-1])
        #     return -reversed_x
        # else:
        #     return int(str(x)[::-1])
        x_str=str(x)
        if x<0:
            x_str=x_str[1:]
            x_str='-'+x_str[::-1]
        else:
            x_str=x_str[::-1]
        res=int(x_str)
        if ((res>(2**31-1)) or (res<-2**31)):
            return 0
        return res