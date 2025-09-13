from collections import Counter
class Solution:
    def maxFreqSum(self, s: str) -> int:
        freq=Counter(s)
        print(freq)
        maxi=0
        maxi1=0
        summ=0
        vowels="aeiou"
        for v in freq:
            if v in vowels:
                maxi=max(maxi,freq[v])
        print(maxi)
        for v in freq:
            if v not in vowels:
                maxi1=max(maxi1,freq[v])
        print(maxi1)
        return maxi+maxi1



