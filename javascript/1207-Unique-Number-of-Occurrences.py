class Solution(object):
    def uniqueOccurrences(self, arr):
        dict1={}
        arr=sorted(arr)
        print(arr)
        for num in arr:
            if num in dict1:
                dict1[num]+=1
            else:
                dict1[num]=1
        print(dict1)
        seen=set()
        for key,value in dict1.items():
            if value in seen:
                return False
            seen.add(value)
        return True