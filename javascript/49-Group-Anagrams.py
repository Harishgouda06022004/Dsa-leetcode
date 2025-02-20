class Solution(object):
    def groupAnagrams(self, strs):
        dict1={}
        for s in strs:
            c=''.join(sorted(s))
            if c not in dict1:
                dict1[c]=[]
            dict1[c].append(s)
        result=list(dict1.values())
        return result