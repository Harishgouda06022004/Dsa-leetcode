class Solution:
    def clearStars(self, s: str) -> str:
        n=len(s)
        pos=[[] for _ in range(26)]
        deleted=[False]*n
        for i,ch in enumerate(s):
            if ch!='*':
                pos[ord(ch)-97].append(i)
            else:
                for j in range(26):
                    if pos[j]:
                        deleted[pos[j].pop()]=True
                        break
        result=[]
        for i,ch in enumerate(s):
            if ch!='*' and not deleted[i]:
                result.append(ch)
        return ''.join(result)