class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # nums.sort()
        # left=0
        # right=len(nums)-1
        # result=[]
        # while left<right:
        #     total=nums[left]+nums[right]
        #     if total==target:
        #         result.append(left)
        #         result.append(right)
        #         left+=1
        #         right-=1
        #     elif total<target:
        #         left+=1
        #     else:
        #         right-=1
        # # unique_list=[list(x) for x in set(tuple(sublist)) for sublist in result]
        # # return unique_list
        # return result
        dict1={}
        result=[]
        for index,num in enumerate(nums):
            complement=target-num
            if complement in dict1:
                # result.append((dict1[complement],index))
                return [dict1[complement],index]
            else:
                dict1[num]=index
                
        return result
        # i = 0
        # while i < len(nums) - 1:
        #     j = i + 1
        #     while j < len(nums):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]
        #         else:
        #             j += 1
        #     i += 1 
        # nums.sort()
        # left=0
        # right=len(nums)-1
        # while left<right:
        #     curr_sum=nums[left]+nums[right]
        #     if curr_sum==target:
        #         return [left,right]
        #     elif curr_sum<target:
        #         left+=1
        #     else:
        #         right-=1
        # return []