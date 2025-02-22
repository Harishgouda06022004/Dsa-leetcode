class Solution(object):
    def repeatedCharacter(self, s):
        dict1={}

        for letter in s:
            if letter in dict1:
                # dict1[letter]=dict1.get(letter,0)+1
                # for key,val in dict1.items():
                #     if val==2:
                #         return key
                return letter
            else:
                dict1[letter]=1
        print(dict1)
        
        # return max(dict1,key=dict1.get)
        