class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # nums=sorted(nums)
        # print(nums)
        n=len(nums)
        # left=0
        # right=n-1
        # while left<right:
        #     mid=(left+right)//2
        #     if nums[mid]==target:
        #         return nums[mid]
        #     elif nums[mid]<target:
        #         left=mid+1
        #     else:
        #         right=mid-1
        # return -1
        for num in range(0,n):
            if nums[num]==target:
                return num
        return -1