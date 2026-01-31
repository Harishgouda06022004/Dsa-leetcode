1class Solution:
2    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
3        left=0
4        right=len(letters)-1
5        if target>=letters[right]:
6            return letters[0]
7        while left<right:
8            mid=(left+right)//2
9            if letters[mid]>target:
10                right=mid
11            elif letters[left]<=target:
12                left=mid+1
13        return letters[left]
14