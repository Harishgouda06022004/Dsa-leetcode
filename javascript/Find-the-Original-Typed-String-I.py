from  collections import Counter
class Solution:
    def possibleStringCount(self, word: str) -> int:
#         word_count=Counter(word)
#         if len(word_count)==1:
#             return len(word)
#         if all(value==1 for value in word_count.values()):
#             return 1
#         count=0
        
#         for value in word_count.values():
#             if value>1:
#                 count+=2
#             else:
#                 count+=1

#         return count
        # word_count=Counter(word)
        # if len(word_count)==1:
        #     return len(word)
        # if all(value==1 for value in word_count.values()):
        #     return 1
        # max_freq=max(word_count.values())
        # return min(max_freq,len(word))
        n=len(word)
        count=n
        for i in range(1,n):
            if word[i]!=word[i-1]:
                count-=1
        return count