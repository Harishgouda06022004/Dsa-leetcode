1class Solution:
2    def furthestDistanceFromOrigin(self, moves: str) -> int:
3        l=r=d=0
4        for c in moves:
5            if c=='L':
6                l+=1
7            elif c=='R':
8                r+=1
9            else:
10                d+=1
11        return abs(l-r)+d