class Solution:
    def isHappy(self, n: int) -> bool:
        # seen=set()
        # curr=str(n)
        # while curr not in seen:
        #     seen.add(curr)
        #     summ=0
        #     for digit in curr:
        #         digit=int(digit)**2
        #         summ+=digit
        #     if summ==1:
        #         return True
        #     curr=str(summ)
        #     print(seen)
        # return False
        seen=set()
        curr=str(n)
        while curr not in seen:
            seen.add(curr)
            summ=0
            for digit in curr:
                digit=int(digit)**2
                summ+=digit
            if summ==1:
                return True
            curr=str(summ)
        return False
