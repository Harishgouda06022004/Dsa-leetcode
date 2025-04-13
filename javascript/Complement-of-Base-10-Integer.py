class Solution:
    def bitwiseComplement(self, n: int) -> int:
        bin_s=bin(n)[2:]
        flipped=''.join('1' if b=='0' else '0' for b in bin_s)
        return int(flipped,2)
