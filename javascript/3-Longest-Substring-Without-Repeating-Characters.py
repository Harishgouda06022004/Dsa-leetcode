class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set=set()
        start=0
        max_lenght=0
        for end in range(len(s)):
            while s[end]  in char_set:
                char_set.remove(s[start])
                start+=1
            char_set.add(s[end])
            max_lenght=max(max_lenght,end-start+1)
        return max_lenght
        