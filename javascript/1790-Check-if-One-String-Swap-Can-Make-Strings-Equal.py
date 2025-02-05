class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1==s2:
            return True
        diff=[]
        for c1,c2 in zip(s1,s2):
            if c1!=c2:
                diff.append((c1,c2))
        if len(diff)!=2:
            return False
        return diff[0] == diff[1][::-1]  
        