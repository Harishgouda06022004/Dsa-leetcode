class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        prefix_sum=0
        min_prefix=0
        max_prefix=0
        for diff in differences:
            prefix_sum+=diff
            min_prefix=min(min_prefix,prefix_sum)
            max_prefix=max(max_prefix,prefix_sum)
        start_min=lower-min_prefix
        start_max=upper-max_prefix
        return max(0,start_max-start_min+1)