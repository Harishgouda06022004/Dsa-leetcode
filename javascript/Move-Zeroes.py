class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        n=len(nums)
        j=0
        for i in range(0,n):
            if nums[i]!=0:
                nums[i],nums[j]=nums[j],nums[i]
                j+=1
        return nums
        