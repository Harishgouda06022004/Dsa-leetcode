class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            complement=target-nums[i]
            if complement in nums[i+1:]:
                return [i,nums.index(complement,i+1)]