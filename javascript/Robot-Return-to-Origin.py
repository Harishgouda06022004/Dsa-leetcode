1from collections import Counter
2class Solution:
3    def judgeCircle(self, moves: str) -> bool:
4        count=Counter(moves)
5        if (count['L']==count['R']) and (count['U']==count['D']):
6            return True
7        return False