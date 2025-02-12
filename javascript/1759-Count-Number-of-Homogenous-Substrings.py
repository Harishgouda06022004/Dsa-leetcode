from collections import Counter
class Solution:
    def countHomogenous(self, s: str) -> int:
        # count=Counter(s)
        # print(count)
        mod=10**9 + 7
        total_count=0
        count=0
        prev=''
        for char in s:
            if char==prev:
                count+=1
            else:
                count=1
            total_count=(total_count+count)%mod
            prev=char
        return total_count
        