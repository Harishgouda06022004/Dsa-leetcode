1class Solution:
2    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
3        n=len(words)
4        ans=float('inf')
5        for i in range(n):
6            if words[i]==target:
7                diff=abs(i-startIndex)
8                distance=min(diff,n-diff)
9                ans=min(ans,distance)
10        return ans if ans!=float('inf') else -1