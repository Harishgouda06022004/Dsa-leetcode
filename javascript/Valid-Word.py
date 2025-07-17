class Solution:
    def isValid(self, word: str) -> bool:
        n=len(word)
        if n<3:
            return False
        vowels=0
        consonants=0
        vowel_set="aeiouAEIOU"
        for c in word:
            if c.isalpha():
                if c in vowel_set:
                    vowels+=1
                else:
                    consonants+=1
            elif not c.isdigit():
                return False
        # if vowels>=1 and consonants>=1:
        #     return True
        # if consonants>=1:
        #     return False
        # if vowels>=1:
        #     return False
        return vowels>=1 and consonants>=1
