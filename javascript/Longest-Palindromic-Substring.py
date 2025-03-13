class Solution:
    def expandAroundCenter(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]
    def longestPalindrome(self, s: str) -> str:
        # def palindrome(t):
        #     n=len(t)
        #     left=0
        #     right=n-1
        #     while left<=right:
        #         if t[left]==t[right] :
        #             left+=1
        #             right-=1
        #         else:
        #             return False
        #     return True
        # n=len(s)
        # longest=\\
        # for i in range(n):
        #     for j in range(i,n):
        #         t=s[i:j+1]
        #         if palindrome(t) and len(t)>len(longest):
        #             longest=t
        # return longest
       
        n = len(s)
        if n <= 1:
            return s
        
        longest = \\
        for i in range(n):
            # Odd length palindrome
            odd_palindrome = self.expandAroundCenter(s, i, i)
            if len(odd_palindrome) > len(longest):
                longest = odd_palindrome
            
            # Even length palindrome
            even_palindrome = self.expandAroundCenter(s, i, i + 1)
            if len(even_palindrome) > len(longest):
                longest = even_palindrome
        
        return longest


        
    