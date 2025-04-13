class Solution:
    def isPalindrome(self, x: int) -> bool:
        # if x<0:
        #     return False
        # return str(x)==str(x)[::-1]
        if x<0:
            return False
        rev=0
        orginal_x=x
        # sign=-1 if x<0 else +1
        while x>0:
            digit=x%10
            rev=rev*10+digit
            x=x//10
        return orginal_x==rev 


            