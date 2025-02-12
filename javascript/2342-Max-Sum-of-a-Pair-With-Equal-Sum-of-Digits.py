from collections import defaultdict
class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        def digitsum(n):
            return sum(int(digit) for digit in str(n))
        digit_map={}
        for num in nums:
            s=digitsum(num)
            # print(f"Number {num} and Digit_Sum {s}")
            if s not in digit_map:
                digit_map[s]=[]
            digit_map[s].append(num)
        print(digit_map)
        max_sum=-1
        for key,value in digit_map.items():
            if len(value)>1:
                value.sort(reverse=True)
                max_sum=max(max_sum,value[0]+value[1])
        return max_sum



