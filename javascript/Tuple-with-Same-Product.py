class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        product_dict={}
        n=len(nums)
        count=0
        for i in range(n):
            for j in range(i+1,n):
                product=nums[i]*nums[j]
                if product in product_dict:
                    product_dict[product]+=1
                else:
                    product_dict[product]=1
        print(product_dict)
        for freq in product_dict.values():
            if freq>1:
                count+=(freq*(freq-1)//2)*8
        return count