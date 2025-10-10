class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        rigth=len(nums)
        while left<rigth:
            mid=(left+rigth)//2
            if nums[mid]<target:
                left+=1
            else:
                rigth=mid
        return left