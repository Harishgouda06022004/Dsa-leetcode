class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # count=0
        # n=len(nums)        
        # for i in range(0,n):
        #     if nums[i]==k:
        #         count+=1
        #     curr_sum=nums[i]
        #     for j  in range(i+1,n):
        #         curr_sum+=nums[j]
        #         if curr_sum==k:
        #             count+=1
        # return count
        count=0
        prefix_sum=0
        prefix_sum_count={0:1}
        for num in nums:
            prefix_sum+=num
            remove=prefix_sum-k
            count+=prefix_sum_count.get(remove,0)
            prefix_sum_count[prefix_sum]=prefix_sum_count.get(prefix_sum,0)+1
        return count

