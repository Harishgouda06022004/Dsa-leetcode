1class Solution:
2    def numOfStrings(self, patterns: List[str], word: str) -> int:
3        count=0
4        for w in patterns:
5            if w in word:
6                count+=1
7        return count