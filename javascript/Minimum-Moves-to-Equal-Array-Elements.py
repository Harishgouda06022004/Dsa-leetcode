class Solution:
    def minMoves(self, nums: List[int]) -> int:
        min_nums=min(nums)
        moves=0
        return sum(num-min_nums for num in nums)
        # for num in nums:
        #     diff=num-min_nums
        #     moves+=diff
        #     print(f\num: {num}, min_num: {min_nums}, num - min_num: {diff}, moves so far: {moves}\)
        # return moves
        moves=0
        # if len(set(nums))==1:
        #     return 