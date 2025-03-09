class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        count=0
        max_count=0
        n=len(colors)
        valid_groups=0
        for i in range(k-1):
            if colors[i]!=colors[(i+1)%n]:
                count+=1
        if count == k - 1: 
            valid_groups += 1
        print(count)
        max_count=count
        n=len(colors)
        for i in range(1,n):
            removeIndex=i-1
            addIndex=(i+k-1)%n
            if colors[removeIndex]!=colors[(removeIndex+1)%n]:
                count-=1
            if colors[addIndex]!=colors[(addIndex-1+n)%n]:
                count+=1
            if count == k - 1:  
                valid_groups += 1
        return valid_groups
            