class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        total=0
        n=len(nums)
        for mask in range(1<<n):
            xor_total=0
            for i in range(n):
                if mask & (1<<i):
                    xor_total^=nums[i]
            total+=xor_total
        return total