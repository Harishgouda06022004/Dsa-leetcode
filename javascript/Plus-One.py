class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num=int(''.join(map(str,digits)))
        print(num)
        num=num+1
        print(num)
        num=str(num)
        print(num)
        num=list(map(int ,str(num)))
        print(num)
        return num
        