class Solution:
    def numTilings(self, n: int) -> int:
        MOD=10**9 + 7
        if n==0:
            return 0
        if n==1:
            return 1
        if n==2:
            return 2
        dp=[0]*(n+1)
        dp[0]=1
        dp[1]=1
        dp[2]=2
        for i in range(3,n+1):
            dp[i]=(2*dp[i-1]+dp[i-3])%MOD
        return dp[n]