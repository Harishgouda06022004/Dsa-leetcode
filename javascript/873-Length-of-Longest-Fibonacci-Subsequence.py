class Solution(object):
    def lenLongestFibSubseq(self, arr):
        n=len(arr)
        arr_set=set(arr)
        max_length=0
        for i in range(0,n):
            for j in range(i+1,n):
                x,y=arr[i],arr[j]
                length=2
                while x+y in arr_set:
                    x,y=y,x+y
                    length+=1
                max_length=max(max_length,length)
        return max_length if max_length>=3 else 0