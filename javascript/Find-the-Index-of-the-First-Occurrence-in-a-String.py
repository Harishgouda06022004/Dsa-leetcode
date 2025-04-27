class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
    #    n=len(haystack)
    #    for i in range(0,n):
    #     if needle in haystack:
    #         return i
    #    return -1
        # n = len(haystack)
        # m = len(needle)

        # # Loop through the haystack and check for the needle at each position
        # for i in range(n - m + 1):  # Only need to check up to (n - m + 1)
        #     if haystack[i:i + m] == needle:  # Compare substring of length m with needle
        #         return i
        
        # return -1
        try:
            return haystack.index(needle)
        except:
            return -1
        