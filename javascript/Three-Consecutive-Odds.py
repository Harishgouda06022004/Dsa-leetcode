class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        # def odd(n):
        #     if n%2!=0:
        #         return odd
        for i in range(len(arr)-2):
            if arr[i]%2!=0 and arr[i+1]%2!=0 and arr[i+2]%2!=0:
                return True
        return False
