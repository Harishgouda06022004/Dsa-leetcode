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
        # x_str=x_str[1:]
        # print(x_str)
        if x<0:
            x_str=x_str[1:] #skip the minus sign we use x_str=x_str[1:] see like -123 which will become 123
            print(x_str)
            x_str='-'+x_str[::-1] # then we reattach it here
        # print(x_str)
        else:
            x_str=x_str[::-1]
        
        res=int(x_str)
        if ((res>(2**31-1)) or (res<-2**31)):
            return 0
        return res
        # rev=0
        # sign=-1 if x<0 else +1
        # x=abs(x)
        # while x!=0:
        #     digit=x%10
        #     rev=rev*10+digit
        #     x=x//10
        # rev*=sign
        # if rev>(2**31-1) or rev<-2**31:
        #     return 0
        # return rev