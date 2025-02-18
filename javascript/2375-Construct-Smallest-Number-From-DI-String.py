class Solution:
    def smallestNumber(self, pattern: str) -> str:
        # num="1,2,3,4,5,6,7,8,9"

        # n=len(pattern)
        # for i in range(0,n+1):
        #     if pattern[i]=='I':
        counter=1
        stack=[]
        res=[]
        n=len(pattern)
        # for i in range(0,n):
        #     stack.append(counter)
        #     if pattern[i]=='D':
        #         stack.append(counter+1)
        #     if pattern[i]=='I':
        #         res.append(str(stack.pop()))
           
        # return ''.join(res)
        counter=1
        res=[]
        stack=[]
        n=len(pattern)
        for i in range(n):
            stack.append(counter)
            counter+=1
            if pattern[i]=='I':
                while stack:
                    res.append(str(stack.pop()))
        stack.append(counter)
        while stack:
            res.append(str(stack.pop()))
        return ''.join(res)