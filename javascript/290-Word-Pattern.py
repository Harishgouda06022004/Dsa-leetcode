class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s=s.split()
        print(s)
        n=len(s)
        print(n)
        n1=len(pattern)
        print(n1)
        if n1!=n:
            return False
        mapping={}
        for char,word in zip(pattern,s):
            if char in mapping:
                if mapping[char]!=word:
                    return False
            else:
                if word in mapping.values():
                    return False  # Prevent multiple characters mapping to the same word
                mapping[char] = word 
        return True
# class Solution:
#     def wordPattern(self, pattern: str, s: str) -> bool:
#         s = s.split()  # Split the string into words
#         print(s)
        # n = len(s)
        # print(n)
        # n1 = len(pattern)
        # print(n1)
        
        # # Check if lengths of pattern and words match
        # if n1 != n:
        #     return False
        
        # # Define the mapping
        # mapping = {'a': 'dog', 'b': 'cat'}
        
        # # Iterate through zipped pairs of pattern and words
        # for char, word in zip(pattern, s):
        #     if char in mapping:
        #         # Check if the mapping matches
        #         if mapping[char] != word:
        #             return False
        #     else:
        #         return False  # Character not in predefined mapping
        
        # return True  # All checks passed

