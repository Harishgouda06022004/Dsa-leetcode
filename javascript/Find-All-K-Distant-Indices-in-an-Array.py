class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        n=len(nums)
        res=set()
        for i in range(0,n):
            if nums[i]==key:
                for j in range(max(0,i-k),min(n,i+k+1)):
                    res.add(j)
        return sorted(res)
        # key_indices = [i for i, val in enumerate(nums) if val == key]
        # res = []
        # start = 0
        # n = len(nums)

        # for i in range(n):
        #     # Slide window to remove key_indices that are too far left
        #     while start < len(key_indices) and key_indices[start] < i - k:
        #         start += 1

        #     # Check if current i is within range of a key index
        #     if start < len(key_indices) and abs(i - key_indices[start]) <= k:
        #         res.append(i)

        # return res