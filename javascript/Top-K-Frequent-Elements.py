from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # dict1={}
        # result=[]
        # for key in nums:
        #     dict1[key]=dict1.get(key,0)+1
        
        # d=sorted(dict1.items(),key=lambda x:x[1],reverse=True)
        

        # # for key,value in dict1.items():
        # #     if value==1:
        # #         result.append(key)
        # #     elif value>=2:
        # #          result.append(key)
        # # sorted_items = sorted(dict1.items(), key=lambda x: x[1], reverse=True)
        # result = [item[0] for item in d[:k]]
        # return result
        d=Counter(nums)
        print(d)
        sorted_items=sorted(d.items(),key=lambda item:item[1],reverse=True)
        print(sorted_items)
        t=[k for k,v in sorted_items]
        print(t)
        res=[]
        for item in t[:k]:
         res.append(item)
        return res