class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        min_operations=float('inf')
        current_white=0
        for i in range(k):
            if blocks[i]=='W':
                current_white+=1
        min_operations=current_white
        print(current_white)
        for i in range(k,len(blocks)):
            print(blocks[i])
            if blocks[i]=='W':
                current_white+=1
            if blocks[i-k] =='W':
                current_white-=1
            print(current_white)
            min_operations=min(min_operations,current_white) 
        return min_operations
            