from collections import defaultdict
class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        # n=len(nums)
        # result=0
        # for i in range(0,n):
        #     for j in range(i,n):
        #         good_pairs=0
        #         for x in range(i, j):
        #             for y in range(x+1,j+1):
        #                 if nums[x]==nums[y]:
        #                     good_pairs+=1
        #     if good_pairs>=k:
        #         result+=1
        # return result
        count=defaultdict(int)
        print(count)
        total_pairs=0
        res=0
        left=0
        for right in range(len(nums)):
            total_pairs+=count[nums[right]]
            count[nums[right]]+=1
            while total_pairs>=k:
                res+=len(nums)-right
                count[nums[left]]-=1
                total_pairs-=count[nums[left]]
                left+=1
        return res