class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        # cost.sort()
        # min_cost=0
        # n=len(cost)
        # i=0
        # j=n-1
        # while i<=j:
        #     min_cost+=cost[i]
        #     i-=1
        #     j-=cost[j]
        # print(min_cost)
        cost.sort(reverse=True)
        n1=sum(cost) 
        l=0
        for i in range(2,len(cost),3):
            l+=cost[i]
        return n1-l
