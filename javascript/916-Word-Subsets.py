class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        dict1={}
        for word in words2:
            temp={}
            for char in word:
                temp[char]=temp.get(char,0)+1
            for char,freq in temp.items():
                dict1[char]=max(dict1.get(char,0),freq)
                print(max(dict1.get(char,0),freq))
            print(temp)
        print(dict1)
        result=[]
        for word in words1:
            dict2={}
            for char in word:
                dict2[char]=dict2.get(char,0)+1
            print(dict2)
            is_universal=True
            for key,value in dict1.items():
                if dict2.get(key,0)<value:
                    is_universal=False
                    break
            if is_universal:
                result.append(word)
        return result
        
       