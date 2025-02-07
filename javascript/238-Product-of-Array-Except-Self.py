class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        prefix=[0]*n
        prefix[0]=1
        for i in range(1,n):
            prefix[i]=prefix[i-1]*nums[i-1]
        print(prefix)
        suffix=[0]*n
        suffix[n-1]=1
        for i in range(n-2,-1,-1):
            suffix[i]=suffix[i+1]*nums[i+1]
        print(suffix)
        answers=[0]*n
        for i in range(0,n):
            answers[i]=prefix[i]*suffix[i]
        return answers
        # result=[]
        
        # for i in range(n):
        #     product=1
        #     for j in range(n):
        #         if i!=j:
        #             product*=nums[j]
        #     result.append(product)
        # return result