from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # max_speed=max(piles)
        # ans=max_speed
        # for k in range(1,max_speed+1):
        #     hours=0
        #     for bananas in piles:
        #         hours+=ceil(bananas/k)
        #     if hours==h:
        #         ans=k
        #         break
        # return ans
        low=1
        high=max(piles)
        ans=high
        while low<=high:
            mid=(low+high)//2
            total_hours=0
            n=len(piles)
            for i in range(0,n):
                total_hours+=ceil(piles[i]/mid)
            if total_hours<=h:
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans

