class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        n=len(nums)
        good_pairs=0
        for i in range(0,n):
            for j in range(i+1,n):
                if nums[i]==nums[j] and (i*j)%k==0:
                    good_pairs+=1
        return good_pairs