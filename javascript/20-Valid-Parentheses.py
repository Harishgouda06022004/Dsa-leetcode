class Solution(object):
    def isValid(self, s):
        stack=[]
        for bracket in s:
            if bracket=='(' or bracket=='[' or bracket=='{':
                stack.append(bracket)
                continue
            if not stack:
                return False
            top=stack[-1]
            stack.pop()
            if (bracket==')' and top=='(') or (bracket==']' and top=='[') or (bracket=='}' and top=='{'):
                continue
            else:
                return False
            
        return len(stack)==0
        