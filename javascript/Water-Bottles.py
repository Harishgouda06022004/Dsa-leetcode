1class Solution:
2    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
3        totalDrank=0
4        empty=0
5        while numBottles>0:
6            totalDrank+=numBottles
7            empty+=numBottles
8            numBottles=empty//numExchange
9            empty%=numExchange
10        return totalDrank