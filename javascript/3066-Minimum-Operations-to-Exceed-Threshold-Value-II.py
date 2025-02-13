import heapq
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        # nums.sort()
        # print(nums)
        # x=nums[0]
        # y=nums[1]
        # count=0
        # while nums[0]<k:
        #     x=nums.pop(0)
        #     y=nums.pop(0)
        #     new_val=x*2+y
        #     count+=1
        #     nums.append(new_val)
        #     nums.sort()
        # return count
        heapq.heapify(nums)
        count=0
        while nums[0]<k:
            x=heapq.heappop(nums)
            y=heapq.heappop(nums)
            new_val=x*2+y
            heapq.heappush(nums,new_val)
            count+=1
        return count


        
