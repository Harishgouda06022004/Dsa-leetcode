1class Solution:
2    def plusOne(self, digits: List[int]) -> List[int]:
3        s = ""
4        for num in digits:
5            s += str(num)
6
7        s = int(s) + 1
8        s = str(s)
9
10        arr = []
11        for i in s:
12            arr.append(int(i))  
13        return arr
14