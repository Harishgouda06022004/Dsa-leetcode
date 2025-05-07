class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        # list3=[]
        # for n in list1:
        #     for m in list2:
        #         if n==m:
        #             list3.append(m)
        # print(list3)
        # return list3
        n=len(list1)
        m=len(list2)
        min_index=float('inf')
        list3=[]
        for i in range(n):
            for j in range(m):
                if list1[i]==list2[j]:
                    index_sum=i+j
                    if index_sum<min_index:
                        list3=[list1[i]]
                        min_index=index_sum
                    elif index_sum==min_index:
                        list3.append(list1[i])
        return list3


                
            
