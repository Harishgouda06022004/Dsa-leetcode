class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        dict1={}
        dict2={}
        for i in jewels:
            dict1[i]=dict1.get(i,0)+1
        print(dict1)
        for i in stones:
            dict2[i]=dict2.get(i,0)+1
        print(dict2)
        count=0
        for i in dict2:
            if i in dict1:
                count+=dict2[i]
        return count