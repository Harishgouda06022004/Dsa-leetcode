class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        dict1={}
        for digits in grid:
            for num in digits:
                if num in dict1:
                    dict1[num]+=1
                else:
                    dict1[num]=1
        print(dict1)
        digit=[]
        for key in dict1.keys():
            if dict1[key]>1:
                digit.append(key)
                break
        print(digit)
        sum_keys=sum(dict1.keys())
        print(sum_keys)
        n = len(grid) * len(grid[0]) 
        print(n)  
        expected_sum = n * (n + 1)//2 
        print(expected_sum)
        actual_value=expected_sum-sum_keys  
        digit.append(actual_value)
        return digit