class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # j=0
        # for i in range(len(nums)):
        #     if nums[i]!=val:
        #         print(nums[j])
        #         nums[i],nums[j]=nums[j],nums[i]
        #         print(nums)
        #         j+=1
        # print(nums)
        # print(nums[:j])
        # return j
        k=0
        for num in nums:
            if num!=val:
                nums[k]=num
                k+=1
        return k