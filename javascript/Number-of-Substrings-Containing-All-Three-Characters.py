1class Solution:
2    def numberOfSubstrings(self, s: str) -> int:
3        last_seen={'a':-1,'b':-1,'c':-1}
4        count=0
5        for i, char, in enumerate(s):
6            last_seen[char]=i
7            if last_seen['a']!=-1 and last_seen['b']!=-1 and last_seen['c']!=-1:
8                min_idx=min(last_seen['a'],last_seen['b'],last_seen['c'])
9                count+=min_idx+1
10        return count