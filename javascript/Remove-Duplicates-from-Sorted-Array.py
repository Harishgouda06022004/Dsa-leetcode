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
        n=len(nums)
        i=1
        j=1
        for i in range(1,n):
            if nums[i]!=nums[i-1]:
                nums[j]=nums[i]
                j+=1
        return j

        