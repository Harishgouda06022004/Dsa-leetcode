from collections import defaultdict
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n=len(s)
        print(n)
        char_count=defaultdict(int)
        l=0
        count=0
        for r in range(n):
            char_count[s[r]]+=1
            while len(char_count)==3:
                count+=n-r
                char_count[s[l]]-=1
                if char_count[s[l]]==0:
                    del char_count[s[l]]
                l+=1
        return count
    

            