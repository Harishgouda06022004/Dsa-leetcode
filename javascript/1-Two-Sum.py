class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            compliment=target-nums[i]
            if compliment in nums[i+1:]:
                return [i,nums.index(compliment,i+1)]