class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        list1=[]
        for e in nums:
            list1.append(e*e)
        return sorted(list1)
        