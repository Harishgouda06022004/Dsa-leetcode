1class Solution:
2    def separateDigits(self, nums: List[int]) -> List[int]:
3        arr=[]
4        for num in nums:
5            if num>9:
6                s=str(num)
7                for n in s:
8                    t=int(n)
9                    arr.append(t)
10            else:
11                arr.append(num)
12        return arr