from collections import defaultdict
class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        count=0
        current_count=0
        prefixcounts=defaultdict(int)
        prefixcounts[0]=1
        print(prefixcounts)
        for num in nums:
            if num%modulo==k:
                current_count+=1
            target=(current_count-k)%modulo
            count+=prefixcounts[target]
            prefixcounts[current_count%modulo]+=1
        return count