class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict1={}
        for i in strs:
            s=''.join(sorted(i))
            if s not in dict1:
                dict1[s]=[]
            dict1[s].append(i)
        return list(dict1.values())