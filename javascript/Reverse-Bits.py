1class Solution:
2    def reverseBits(self, n: int) -> int:
3        a = bin(n)[2:].zfill(32)
4        b = a[::-1]
5        c = int(b, 2)
6        return c