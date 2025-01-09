class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
       
        # for char in t:
        #     if char not in s:
        #         return char
        #     if s==t
        #         return char
        dict1={}
        dict2={}
        for char in s:
            if char in dict1:
                dict1[char]+=1
            else:
                dict1[char]=1
        for char in t:
            if char in dict2:
                dict2[char]+=1
            else:
                dict2[char]=1
        for char in dict2:
            if char not in dict1 or dict2[char] > dict1[char]:
                return char
        
