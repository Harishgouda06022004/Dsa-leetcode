class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        n=len(num)
        stack=[]
        for i in range(0,n):
            
            while stack and k>0 and stack[-1]>num[i]:
                stack.pop()
                k-=1
            stack.append(num[i])
        while k>0 and stack:
            stack.pop()
            k-=1
        res = ''.join(stack)
        
    # Remove leading zeros
        res = res.lstrip('0')
    
    # If res is empty, return \0\
        if not res:
            return \0\

        return res
