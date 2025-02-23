class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        # count=0
        # for s in stones:
        #     if s in jewels:
        #         count+=1
        # return count
        count=0
        jewels=set(jewels)
        for s in stones:
            if s in jewels:
                count+=1
        return count