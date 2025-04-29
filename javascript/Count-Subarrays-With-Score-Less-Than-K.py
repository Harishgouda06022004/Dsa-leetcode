class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        left=0
        summ=0
        count=0
        n=len(nums)
        for right in range(n):
            summ+=nums[right]
            while summ*(right-left+1)>=k:
                summ-=nums[left]
                left=left+1
            count+=(right-left+1)
        return count