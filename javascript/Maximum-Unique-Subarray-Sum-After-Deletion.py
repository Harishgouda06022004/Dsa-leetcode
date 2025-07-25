from collections import Counter
class Solution:
    def maxSum(self, nums: List[int]) -> int:
        counter_nums=Counter(nums)
        print(counter_nums)
        summ=0
        all_negative=True
        for key,value in counter_nums.items():
            if key>0:
                summ+=key
                # all_negative=False 
            # if all_negative:
            #     return max(nums)

            # if len(nums)==1:
            #     return nums[0] 
            # if len(nums)==2 and key<0:
            #     return max(nums)  
            if all(k<0 for k in counter_nums.keys()):
                return max(nums)
        return summ
        # left=0
        # seen=set()
        # n=len(nums)
        # max_sum = float('-inf')
        # curr_sum=0
        # for right in range(n):
        #     while nums[right] in seen:
        #         seen.remove(nums[left])
        #         curr_sum-=nums[left]
        #         left+=1
        #     seen.add(nums[right])
        #     curr_sum+=nums[right]
        #     max_sum=max(max_sum,curr_sum)
        # return max_sum

