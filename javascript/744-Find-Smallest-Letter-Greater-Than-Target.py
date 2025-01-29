class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        left=0
        right=len(letters)-1
        if target>=letters[right]:
            return letters[0]
        
        # second=left+1
        while left<right:
            mid=(left+right)//2
            if letters[mid]>target:
                # return letters[left]
                # left+=1
                # right-=1
                right=mid
                # left=mid+1
                # right=mid-1
            elif letters[left]<=target:
                left=mid+1
        return letters[left]
