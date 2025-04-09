class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        operations=0
        greater_than_k=set()
        for i in range(len(nums)):
            if nums[i]<k:
                return -1
            if nums[i]>k and nums[i] not in greater_than_k:
                operations+=1
                greater_than_k.add(nums[i])
        return operations 