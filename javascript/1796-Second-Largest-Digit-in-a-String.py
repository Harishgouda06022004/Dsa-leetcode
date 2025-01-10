class Solution:
    def secondHighest(self, s: str) -> int:

        s=''.join(filter(str.isdigit,s))
        t=set(s)
        if len(t)<2:
            return -1
        n=sorted(t)
        return int(n[-2])