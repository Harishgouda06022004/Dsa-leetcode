class Solution:
    def countElements(self, nums: List[int]) -> int:
        count=0
        n=len(nums)
        nums=sorted(nums)
        print(nums)
        e=min(nums)
        m=max(nums)
        print(n)
        print(m)
        for i in range(0,n):
            if nums[i]>e and nums[i]<m:
                count+=1
        return count