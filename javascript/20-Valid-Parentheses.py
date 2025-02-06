class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        # n=len(s)
        # print(n)
        for i in s:
            if i=='(' or i=='{' or i=='[':
                stack.append(i)
            else:
                if len(stack)==0:
                    return False
                top=stack[-1]
                
                if i==')' and top==\(\ or i==\}\ and top==\{\ or i==\]\ and top==\[\:
                    stack.pop()
                else:
                    return False
        return len(stack)==0
