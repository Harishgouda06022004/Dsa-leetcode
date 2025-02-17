class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l=[x**2 for x in nums]
        l=sorted(l)
        return l
        