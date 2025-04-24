class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        total_distinct=len(set(nums))
        n=len(nums)
        count=0
        for left in range(n):
            seen=set()
            for right in range(left,n):
                seen.add(nums[right])
                if len(seen)==total_distinct:
                    count+=1
        return count 