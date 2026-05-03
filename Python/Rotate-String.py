1class Solution:
2    def rotateString(self, s: str, goal: str) -> bool:
3        if len(s)!=len(goal):
4            return False
5        t=s+s
6        if goal in t:
7            return True
8        return False