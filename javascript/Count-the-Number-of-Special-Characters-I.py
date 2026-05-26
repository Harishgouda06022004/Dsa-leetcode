1class Solution:
2    def numberOfSpecialChars(self, word: str) -> int:
3        spc=set()
4        for char in word:
5            if char.islower() and char.upper() in word:
6                spc.add(char)
7            elif char.isupper() and char.lower() in word:
8                spc.add(char)
9        return len(spc)//2