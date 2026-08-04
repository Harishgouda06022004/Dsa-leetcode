class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        mini=min(nums)
        maxi=max(nums)
        seen=set(nums)
        ans=[]
        for x in range(mini+1,maxi):
            if x not in seen:
                ans.append(x)
        return ans