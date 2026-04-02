1class Solution:
2    def removeElement(self, nums: List[int], val: int) -> int:
3        k=0
4        for num in nums:
5            if num!=val:
6                nums[k]=num
7                k+=1
8        return k