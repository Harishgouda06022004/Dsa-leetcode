class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        sum_of_n_natural_numbers=n*(n+1)/2
        sum_of_nums=0
        for num in nums:
            sum_of_nums+=num
        missing_number=sum_of_n_natural_numbers-sum_of_nums
        return int(missing_number)
        
