class Solution:
    def countAndSay(self, n: int) -> str:
        if n==1:
            return \1\
        prev=self.countAndSay(n-1)
        return self.rle(prev)
    def rle(self,s:str)->str:
        sb=[]
        n=len(s)
        count=1
        for i in range(1,n):
            if s[i]==s[i-1]:
                count+=1
            else:
                sb.append(str(count))
                sb.append(s[i-1])
                count=1
        print(sb)
        sb.append(str(count))
        sb.append(s[-1])
        return \\.join(sb)
