class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # seen=set()
        # index=0
        # for num in nums:
        #     if num not in seen:
        #         seen.add(num)
        #         nums[index]=num
        #         index+=1
        # return index
        # n=len(nums)
        # j=1
        # for i in range(1,n):
        #     print(nums[i])
        #     if nums[i]!=nums[i-1]:
        #         print(nums[i],nums[i-1])
        #         nums[j]=nums[i]
        #         j+=1
        # return j
        # seen=set()
        # index=0
        # for num in nums:
        #     if num not in seen:
        #         seen.add(num)
        #         nums[index]=num
        #         index+=1
        # return index
        # seen=set()
        # n=len(nums)
        # index=n-1
        # for i in range(n-1,-1,-1):
        #     if nums[i] not in seen:
        #         seen.add(nums[i])
        #         nums[index]=nums[i]
        #         index-=1
        # return n-(index+1)
        #Simple two pointer
        n=len(nums)
        j=1 # we skip first number because its only one we can reduce iterations here
        for i in range(1,n): # we loop from 1 to till last element of array
            if nums[i]!=nums[i-1]: # if two nums are not equal 
                nums[j]=nums[i] # we replace duplicate  number with that new number
                j+=1 # then we update out another pointer
        return j # we return that index where duplicates are not presnt and the sorted array does not consisit of duplicate ones


        