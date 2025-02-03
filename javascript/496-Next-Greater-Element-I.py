class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result=[]
        for num in nums1:
            index=nums2.index(num)
            nums_greater=-1
            for j in range(index+1,len(nums2)):
                if nums2[j]>num:
                    nums_greater=nums2[j]
                    break
            result.append(nums_greater)
        return result
