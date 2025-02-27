class Solution(object):
    def lenLongestFibSubseq(self, arr):
        n=len(arr)
        arr_set=set(arr)
        max_lenght=0
        for i in range(0,n):
            for j in range(i+1,n):
                x,y=arr[i],arr[j]
                lenght=2
                while x+y in arr_set:
                    x,y=y,x+y
                    lenght+=1
                max_lenght=max(max_lenght,lenght)
        return max_lenght if max_lenght>=3 else 0