class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result=[]
        for i in range(len(nums)):
            left=i+1
            right=len(nums)-1
            while left<right:
                total=nums[i]+nums[left]+nums[right]
                if total==0:
                    result.append([nums[i],nums[left],nums[right]])
                    left+=1
                    right-=1
                    while left<right and nums[left]==nums[left-1]:
                        left+=1
                    while left<right and nums[right]==nums[right+1]:   
                        right-=1
                elif total<0:
                    left+=1
                else:
                    right-=1
        # unique_list=[]
        # for sublist in result:
        #     sublist_tuple=tuple(sublist)
        #     if sublist_tuple not in unique_list:
        #         unique_list.append(sublist_tuple)
        # unique_list =[list(x) for x in unique_list]
        # return unique_list

        unique_list = [list(x) for x in set(tuple(sublist) for sublist in result)]
        return unique_list
       
      
       