class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        n=len(s)
        result=[]
        t=""
        for i in range(0,n):
            t+=s[i]
            if len(t)==k:
                result.append(t)
                t=""
        if t:
            t+=fill*(k-len(t))
            result.append(t)
        return result