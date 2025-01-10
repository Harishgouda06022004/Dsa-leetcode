class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        dict1={}
        for char in s:
            if char in dict1:
                dict1[char]+=1
            else:
                dict1[char]=1
        if len(set(dict1.values()))==1:
            return True
        else:
            return False