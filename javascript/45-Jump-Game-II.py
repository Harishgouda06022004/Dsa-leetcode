class Solution:
    def jump(self, nums: List[int]) -> int:
        target=len(nums)-1
        count=0
        while target>0:
            for i in range(target):
                if i+nums[i]>=target:
                    target=i
                    count+=1
                    break
        return count