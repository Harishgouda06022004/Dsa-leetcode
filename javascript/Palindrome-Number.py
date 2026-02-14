1class Solution:
2    def isPalindrome(self, x: int) -> bool:
3        if x<0:
4            return False
5        rev=0
6        orginal_x=x
7        # sign=-1 if x<0 else +1
8        while x>0:
9            digit=x%10
10            rev=rev*10+digit
11            x=x//10
12        return orginal_x==rev 