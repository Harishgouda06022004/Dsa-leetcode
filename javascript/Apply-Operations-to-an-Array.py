class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n=len(nums)
        for i in range(0,n-1):
            if nums[i]==nums[i+1]:
                nums[i]=nums[i]*2
                nums[i+1]=0
        print(nums)
        pos=0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[i],nums[pos]=nums[pos],nums[i]
                pos+=1
        return nums