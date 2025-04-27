class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # words=s.split()
        # print(words)
        # return len(words[-1])
        words=[]
        word=\\
        for char in s:
            if char!=\ \:
                word+=char
            else:
                if word:
                    words.append(word)
                    word=\\
        if word:
            words.append(word)
        print(words)
        return len(words[-1])