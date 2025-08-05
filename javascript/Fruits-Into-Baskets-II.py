class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        used=[False]*len(baskets)
        count=0
        for fruit in fruits:
            placed=False
            for i in range(len(baskets)):
                if not used[i] and baskets[i]>=fruit:
                    used[i]=True
                    placed=True
                    break
            if not placed:
                count+=1
        return count