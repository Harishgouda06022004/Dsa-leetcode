# class Solution:
#     def isValid(self, s: str) -> bool:
#         stack = []
#         mapping = {"(":")",
#                    "[":"]",
#                    "{":"}"}
#         for char in s:
#             if char in mapping.keys():
#                 stack.append(char)
#                 print(stack)
#             elif char in mapping.values():
#                 if not stack or  mapping.get(stack.pop()) != char:
#                     return False
#         return not stack
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {"(": ")", "[": "]", "{": "}"}

        for char in s:
            if char in mapping:  # Check for opening brackets
                stack.append(char)
            elif char in mapping.values():  # Check for closing brackets
                if not stack or mapping[stack.pop()] != char:  # Pop from stack and match
                    return False

        return not stack  # If stack is empty, return True (all brackets matched)
       
        
        