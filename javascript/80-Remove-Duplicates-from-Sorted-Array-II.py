class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        dict1=Counter(nums)
        for key, value in dict1.items():
            if value>2:
                dict1[key]=2
        t=[]
        for key,value in dict1.items():
            for i in range(value):
                t.append(key)
        for i in range(len(t)):
            nums[i]=t[i]
        return len(t)