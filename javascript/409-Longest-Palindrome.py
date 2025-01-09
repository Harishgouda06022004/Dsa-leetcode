class Solution:
    def longestPalindrome(self, s: str) -> int:
        dicti={}
        for char in s:
            if char in dicti:
                dicti[char]+=1
            else:
                dicti[char]=1
        length=0
        odd_found=False
        for count in dicti.values():
            if count%2==0:
                length+=count
                
            else:
                length+=count-1
                odd_found=True
        if odd_found:
            length+=1
        return length