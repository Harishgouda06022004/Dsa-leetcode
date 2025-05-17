class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # target=len(nums)-1
        # for i in range(len(nums)):
        #     if nums[i]>0:
        #         return True
        #     else:
        #         return False
        # target=len(num)-1
        # for num in nums:
        #     if num==0:
        #         return False
        target=len(nums)-1
        for i in range(len(nums)-2,-1,-1):
            if i+nums[i]>=target:
                target=i    
        return target==0
        target=len(nums)-1
        for i in range(len(nums)-2,-1,-1):
            if i+nums[i]>=target:
                target=i
                
        return  target==0
        # max_reach=0
        # for i in range(len(nums)):
        #     if i>max_reach:
        #         return False
        #     max_reach=max(max_reach,i+nums[i])
        # return True