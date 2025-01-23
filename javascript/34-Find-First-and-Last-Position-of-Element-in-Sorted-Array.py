class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def firstOccur(nums,target):
            left=0
            right=len(nums)-1
            first_pos=-1
            while left<=right:
                mid=(left+right)//2
                if nums[mid]==target:
                    first_pos=mid
                    right=mid-1
                elif nums[mid]<target:
                    left=mid+1
                else:
                    right=mid-1
            return first_pos
        def second_occur(nums,target):
            left=0
            right=len(nums)-1
            second_pos=-1
            while left<=right:
                mid=(left+right)//2
                if nums[mid]==target:
                    second_pos=mid
                    left=mid+1
                elif nums[mid]<target:
                    left=mid+1
                else:
                    right=mid-1
            return second_pos
        first_pos=firstOccur(nums,target)
        second_pos=second_occur(nums,target)
        return [first_pos,second_pos]
        