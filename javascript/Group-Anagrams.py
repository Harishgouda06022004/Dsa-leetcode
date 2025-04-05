class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict1={}
        for i in strs:
            s=''.join(sorted(i))
            # print(s)
            if s not in dict1:
                dict1[s]=[]
                print(dict1)
            dict1[s].append(i)
            print(dict1)
        return list(dict1.values())