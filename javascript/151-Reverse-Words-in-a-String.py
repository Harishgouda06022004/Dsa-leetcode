class Solution:
    def reverseWords(self, s: str) -> str:
        t=s.split()

        return \ \.join(t[::-1])