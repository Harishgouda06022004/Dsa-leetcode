class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        # count=0
        # for num in hours:
        #     if num>=target:
        #         count+=1
        # return count
        return sum(num>=target for num in hours)