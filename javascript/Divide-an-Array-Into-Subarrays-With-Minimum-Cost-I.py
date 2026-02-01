1class Solution:
2    def minimumCost(self, nums: List[int]) -> int:
3        m1,m2=float('inf'),float('inf')
4        for n in nums[1:]:
5            m2=min(m2,n)
6            if m2<m1:
7                m1,m2=m2,m1
8        return nums[0]+m1+m2