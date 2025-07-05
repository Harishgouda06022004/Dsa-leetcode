from collections import Counter
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        arr_freq=Counter(arr)
        print(arr_freq)
        max_lucky=-1
        for key,value in arr_freq.items():
            
            print(max_lucky)
            if key==value:
                max_lucky=max(max_lucky,key)
        return max_lucky
        