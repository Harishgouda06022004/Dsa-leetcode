class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dict1={}
        # result=[]
        for index,num in enumerate(numbers):
            compliment=target-num
            if compliment in dict1:
                return [dict1[compliment]+1,index+1]
            else:
                dict1[num]=index
        # return 