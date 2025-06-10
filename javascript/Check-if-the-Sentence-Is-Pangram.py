class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        # sentence=sentence.lower()
        # unique_letters=set(char for char in sentence if char.isalpha())
        # return len(unique_letters)==26
        return len(set(sentence))==26
        