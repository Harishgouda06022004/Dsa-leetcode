from collections import Counter
class Solution:
    def maxDifference(self, s: str) -> int:
        t=Counter(s)
        print(t)
        e=[]
        o=[]
        for i in t.values():
            if i%2==0:
                e.append(i)
            else:
                o.append(i)
        return max((-max(e)+min(o)),(max(o)-min(e)))
