class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words=[]
        word=""
        for char in s:
            if char!=" ":
                word+=char
            else:
                if word:
                    words.append(word)
                    word=""
        if word:
            words.append(word)
        return len(words[-1])