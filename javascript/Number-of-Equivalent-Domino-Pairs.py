from collections import defaultdict
class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        # n=len(dominoes)
        # count=0
        # for i in range(n):
        #     for j in range(i+1,n):
        #         a,b=dominoes[i]
        #         c,d=dominoes[j]
        #         if (a==c and b==d) or (a==d and b==c):
        #             count+=1
        # return count
        count=0
        freq=defaultdict(int)
        for a,b in dominoes:
            key=tuple(sorted((a,b)))
            count+=freq[key]
            freq[key]+=1
        return count