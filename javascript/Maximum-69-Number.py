class Solution:
    def maximum69Number (self, num: int) -> int:
        s=str(num)
        i=-1
        for j in range(len(s)):
            if s[j]=='6':
                i=j
                break
        if i==-1:
            return num
        else:
            return int(s[:i]+'9'+s[i+1:])