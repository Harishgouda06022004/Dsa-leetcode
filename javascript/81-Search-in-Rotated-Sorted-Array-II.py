class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        n=len(nums)
        for num in range(0,n):
            if nums[num]==target:
                return True
        return False