class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        left,right=1,min(ranks)*(cars**2)
        def canRepairTime(time):
            total_cars=0
            for r in ranks:
                total_cars+=int((time/r)**0.5)
            return total_cars>=cars
        while left<right:
            mid=(left+right)//2
            if canRepairTime(mid):
                right=mid
            else:
                left=mid+1
        return left