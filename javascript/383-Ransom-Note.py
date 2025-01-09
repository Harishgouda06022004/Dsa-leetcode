class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dict1={}
        for s in magazine:
            if s in dict1:
                dict1[s]+=1
            else:
                dict1[s]=1
        for char in ransomNote:
            if char not in dict1 or dict1[char]==0:
                return False
            dict1[char] -= 1
        return True 