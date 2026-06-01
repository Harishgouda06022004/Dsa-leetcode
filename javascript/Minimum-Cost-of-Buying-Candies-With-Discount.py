1class Solution:
2    def minimumCost(self, cost: List[int]) -> int:
3        cost.sort(reverse=True)
4        n1=sum(cost) 
5        l=0
6        for i in range(2,len(cost),3):
7            l+=cost[i]
8        return n1-l