class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        n=len(words)
        result=[]
        for word in range(n):
            for w in words[word]:
                if w==x:
                    result.append(word)
                    break
        print(result)
        return result