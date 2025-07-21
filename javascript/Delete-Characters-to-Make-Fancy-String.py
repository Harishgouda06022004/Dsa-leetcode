# from collections import Counter
class Solution:
    def makeFancyString(self, s: str) -> str:
        # counter_s=Counter(s)
        # print(counter_s)
        res=""
        for i in range(len(s)):
            if i>=2 and s[i]==s[i-1]==s[i-2]:
                continue
            res+=s[i]
        print(res)
        return res

        