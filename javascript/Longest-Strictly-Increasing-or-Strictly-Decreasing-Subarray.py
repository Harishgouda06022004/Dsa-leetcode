class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        n=len(nums)
        inc=1
        dec=1
        max_length=1
        if n<=1:
            return 1
        for i in range(0,n-1):
            if nums[i]<nums[i+1]:
                inc+=1
                dec=1
            elif nums[i]>nums[i+1]:
                dec+=1
                inc=1
            else:
                inc=dec=1
            max_length=max(max_length,inc,dec)
        return max_length
