from collections import Counter
class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        # sort=[]
        # for word in words:
        #     sorted_word=''.join(sorted(word))
        #     sort.append(sorted_word)
        # print(sort)
        # s=Counter(sort)
        # print(s)
        # t=[]
        # for key in s.keys():
        #     t.append(key)
        # return t
        res=[words[0]]
        for i in range(1,len(words)):
            if sorted(words[i])!=sorted(words[i-1]):
                res.append(words[i])
        return res
