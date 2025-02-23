class Solution(object):
    def groupAnagrams(self, strs):
        dict1={}
        for s in strs:
            c=''.join(sorted(s))
            if c not in dict1:
                dict1[c]=[]
            dict1[c].append(s)
        # print(dict1)
        # result=list(dict1.values())
        return dict1.values()
        # dict1={}
        # for s in strs:
        #     s_sorted=sorted(s)
        #     key=tuple(s_sorted) #keeping it in tuple form form because key are always immutable
        #     if key not in dict1:
        #         dict1[key]=[s]
        #     else:
        #         dict1[key].append(s)
        # return dict1.values()