class Solution:
    def minimumPushes(self, word: str) -> int:
        freq = Counter(word)
        print(freq)
        counts = sorted(freq.values(), reverse=True)
        print(counts)
        pushes=0
        for i,count in enumerate(counts):
            pushes+=count*((i//8)+1)
            print(f"count={count} * (({i}//8)+1) = {count * ((i//8)+1)}")
        return pushes