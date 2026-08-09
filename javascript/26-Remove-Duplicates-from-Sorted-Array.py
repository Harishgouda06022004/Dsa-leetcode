from collections import Counter
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n=Counter(nums)
        print(n)
        t=list(n.keys())
        for i in range(len(t)):
            nums[i] = t[i]
        return len(t)