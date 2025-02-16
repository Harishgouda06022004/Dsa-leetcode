class Solution:
    def isHappy(self, n: int) -> bool:
        seen=set()
        curr=str(n)
        while curr not in seen:
            seen.add(curr)
            summ=0
            for digit in curr:
                digit=int(digit)
                summ+=digit**2
            if summ==1:
                return True
            curr=str(summ)   
        return False