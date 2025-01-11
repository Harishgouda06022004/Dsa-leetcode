class Solution:
    def sortSentence(self, s: str) -> str:
       s=s.split()
       sorted_words=sorted(s,key=lambda word:word[-1])
       return " ".join([''.join([char for char in word if not char.isdigit()]) for word in sorted_words])