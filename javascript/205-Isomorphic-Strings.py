class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dict1={}
        dict2={}
       
        for char_s,char_t in zip(s,t):
            if char_s in dict1:
                if dict1[char_s]!=char_t:
                    return False
            if char_t in dict2:
                if dict2[char_t]!=char_s:
                    return False
            dict1[char_s]=char_t
            dict2[char_t]=char_s
        return True