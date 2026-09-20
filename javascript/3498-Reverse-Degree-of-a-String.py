class Solution:
    def reverseDegree(self, s: str) -> int:
        ans=0
        n=len(s)
        for i in range(n):
            x=26-(ord(s[i])-ord('a'))
            ans+=(i+1)*x
        return ans