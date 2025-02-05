class StockSpanner:

    def __init__(self):
        self.stack=[]

    def next(self, price: int) -> int:
        # self.stack.append(price)
        # print(self.stack)
        # cnt=1
        # for i in range(len(self.stack)-2,-1,-1):
        #     if self.stack[i]<=price:
        #         cnt+=1
        #     else:
        #         break
        # return cnt
        cnt=1
        while self.stack and self.stack[-1][0]<=price:
            cnt+=self.stack.pop()[1]
        self.stack.append((price,cnt))
        return cnt
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)