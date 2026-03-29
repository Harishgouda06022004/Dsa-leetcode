1class Solution:
2    def canBeEqual(self, s1: str, s2: str) -> bool:
3        return ((s1[0] == s2[0] and s1[2] == s2[2]) or
4                (s1[0] == s2[2] and s1[2] == s2[0])) and \
5               ((s1[1] == s2[1] and s1[3] == s2[3]) or
6                (s1[1] == s2[3] and s1[3] == s2[1]))