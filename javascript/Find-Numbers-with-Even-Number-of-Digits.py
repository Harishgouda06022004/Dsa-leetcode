class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count=0
        for num in nums:
            n=len(str(num))
            if n%2==0:
                count+=1
        print(count)
        return count