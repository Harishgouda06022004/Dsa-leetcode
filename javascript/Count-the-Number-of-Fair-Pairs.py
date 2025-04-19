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
# class Solution:
#     def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
#         def upperbound(arr, target, end):
#             left = 0
#             right = end
#             print(f"upperbound: Searching for target {target} in arr[:{end}]")
#             while left < right:
#                 mid = (left + right) // 2
#                 print(f"upperbound: left={left}, right={right}, mid={mid}, arr[mid]={arr[mid]}")
#                 if arr[mid] <= target:
#                     left = mid + 1
#                 else:
#                     right = mid
#             print(f"upperbound: Resulting left={left}")
#             return left

#         def lowerbound(arr, target, end):
#             left = 0
#             right = end
#             print(f"lowerbound: Searching for target {target} in arr[:{end}]")
#             while left < right:
#                 mid = (left + right) // 2
#                 print(f"lowerbound: left={left}, right={right}, mid={mid}, arr[mid]={arr[mid]}")
#                 if arr[mid] < target:
#                     left = mid + 1
#                 else:
#                     right = mid
#             print(f"lowerbound: Resulting left={left}")
#             return left

#         # Sort the array first
#         nums.sort()
#         print(f"Sorted nums: {nums}")
#         n = len(nums)
#         count = 0

#         # For each number in the sorted array, calculate the fair pairs
#         for i in range(n):
#             print(f"\nConsidering nums[{i}] = {nums[i]}:")
#             low = lowerbound(nums, lower - nums[i], i)
#             high = upperbound(nums, upper - nums[i], i)
#             print(f"Range for nums[{i}] = {nums[i]}: lowerbound={low}, upperbound={high}")
#             count += (high - low)
#             print(f"Current count: {count}")

#         return count
      
