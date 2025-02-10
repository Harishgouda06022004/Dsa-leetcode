# class Solution:
#     def countBadPairs(self, nums: List[int]) -> int:
#         count=0
#         n=len(nums)
#         for  i in range(0,n):
#             for j in range(i+1,n):
#                 if i < j and j - i != nums[j] - nums[i]:
#                     count+=1
#         return count
from collections import defaultdict

class Solution:
    def countBadPairs(self, nums):
        # HashMap to store frequency of (nums[i] - i)
        freq = defaultdict(int)
        good_pairs = 0
        
        for i in range(len(nums)):
            diff = nums[i] - i
            good_pairs += freq[diff]  # Count how many times this diff appeared earlier
            freq[diff] += 1  # Increase the count for this diff

        total_pairs = len(nums) * (len(nums) - 1) // 2
        return total_pairs - good_pairs  # Bad pairs = Total pairs - Good pairs
