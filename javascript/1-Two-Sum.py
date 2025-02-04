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
        for index,i in enumerate(nums):
            complement=target-i
            if complement in dict1:
                return [index,dict1[complement]]
            dict1[i]=index
        return []