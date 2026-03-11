1class Solution:
2    def bitwiseComplement(self, n: int) -> int:
3        bin_s=bin(n)[2:]
4        flipped=''.join('1' if b=='0' else '0' for b in bin_s)
5        return int(flipped,2)