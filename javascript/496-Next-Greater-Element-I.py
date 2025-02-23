class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        greater=[]
        for num in nums1:
            next_greater=-1
            index=nums2.index(num)
            for j in range(index+1,len(nums2)):
                if nums2[j]>num:
                    next_greater=nums2[j]
                    break
            greater.append(next_greater)
        return greater