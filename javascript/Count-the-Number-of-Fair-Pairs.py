class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        def upperbound(arr,target,end):
            left=0
            right=end
            while left<right:
                mid=(left+right)//2
                if arr[mid]<=target:
                    left=mid+1
                else:
                    right=mid
            return left
        def lowerbound(arr,target,end):
            left=0
            right=end
            while left<right:
                mid=(left+right)//2
                if arr[mid]<target:
                    left=mid+1
                else:
                    right=mid
            return left
        nums.sort()
        n=len(nums)
        count=0
        for i in range(n):
            low=lowerbound(nums,lower-nums[i],i)
            high=upperbound(nums,upper-nums[i],i)
            count+=(high-low)
        return count
        
