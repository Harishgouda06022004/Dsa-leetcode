class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        result=[]
        
        dict2={}
        dict1={}
        for num in range(len(A)):
            dict1[A[num]]=dict1.get(A[num],0)+1
            dict2[B[num]]=dict2.get(B[num],0)+1
            count=0
            for key in dict1:
                if key in dict2:
                    count+=1
            result.append(count)
        return result
        
                