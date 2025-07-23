class Solution:
    def makeFancyString(self, s: str) -> str:
        res=""
        for i in range(len(s)):
            if i>=2 and s[i]==s[i-1]==s[i-2]:
                continue
            res+=s[i]
        return res

        