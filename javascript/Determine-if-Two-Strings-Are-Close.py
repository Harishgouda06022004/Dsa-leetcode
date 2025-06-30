from collections import Counter
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        word1_counter=Counter(word1)
        word2_counter=Counter(word2)
        print(word1_counter)
        print(word2_counter)
        if word1_counter.keys()!=word2_counter.keys():
            return False
        return sorted(word1_counter.values())==sorted(word2_counter.values())