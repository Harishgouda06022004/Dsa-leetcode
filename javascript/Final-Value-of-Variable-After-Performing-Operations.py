class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x=0
        for v in operations:
            if v=="++X":
                x+=1
            elif v=="X++":
                x+=1
            elif v=="--X":
                x-=1
            elif v=="X--":
                x-=1
        return x