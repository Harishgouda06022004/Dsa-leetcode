class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        zeroN1=0
        zeroN2=0
        sum1=0
        sum2=0
        for n in nums1:
            if n==0:
                zeroN1+=1
            else:
                sum1+=n
        for n in nums2:
            if n==0:
                zeroN2+=1
            else:
                sum2+=n
        min1=zeroN1+sum1
        min2=zeroN2+sum2
        if zeroN1 == 0 and zeroN2 == 0:
            return sum1 if sum1 == sum2 else -1
        elif zeroN1 == 0:
            return sum1 if sum2 + zeroN2 <= sum1 else -1
        elif zeroN2 == 0:
            return sum2 if sum1 + zeroN1 <= sum2 else -1
        else:
            return max(min1, min2)

