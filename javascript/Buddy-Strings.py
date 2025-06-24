from collections import Counter
class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        n=len(s)
        g=len(goal)
        if n!=g:
            return False
        if s == goal:
            freq = Counter(s)
            for count in freq.values():
                if count >= 2:
                    return True
            return False
        diff=[]
        for st,ts in zip(s,goal):
            if st!=ts:
                diff.append((st,ts))
        print(diff)
        return len(diff) == 2 and diff[0] == diff[1][::-1]


        
        