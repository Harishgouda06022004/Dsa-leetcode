class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        result=set()
        for a,b,c in permutations(digits,3):
            if a==0:
                continue
            if c%2!=0:
                continue
            num=100*a+10*b+c
            result.add(num)

        return sorted(result)