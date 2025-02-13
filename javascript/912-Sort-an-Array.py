class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # if len(nums)<=1:
        #     return nums
        # pivot=nums[-1]
        # print(pivot)
        # left=[x for x in nums[:-1] if x<=pivot]
        # right=[x for x in nums[:-1] if x>pivot]
        # return self.sortArray(left)+[pivot]+self.sortArray(right)
        s=sorted(nums)
        return s