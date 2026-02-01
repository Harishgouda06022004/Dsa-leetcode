1class Solution:
2    def minimumCost(self, nums: List[int]) -> int:
3        # print("Input nums:", nums)
4
5        # m1, m2 = float('inf'), float('inf')
6        # print("Initial m1:", m1, "m2:", m2)
7
8        # for n in nums[1:]:
9        #     print("\nCurrent n:", n)
10
11        #     # Update m2
12        #     m2 = min(m2, n)
13        #     print("After m2 = min(m2, n) -> m2:", m2)
14
15        #     # Ensure m1 is always the smallest
16        #     if m2 < m1:
17        #         print("m2 < m1, so swapping m1 and m2")
18        #         m1, m2 = m2, m1
19
20        #     print("Current m1:", m1, "m2:", m2)
21
22        # result = nums[0] + m1 + m2
23        # print("\nFinal calculation:")
24        # print("nums[0]:", nums[0], "m1:", m1, "m2:", m2)
25        # print("Result:", result)
26
27        # return result
28        rest=sorted(nums[1:])
29        return nums[0]+rest[0]+rest[1]