class Solution:
    def trap(self, height: List[int]) -> int:
        # left=0
        # right=len(height)-1
        # left_max=height[left]
        # right_max=height[right]
        # water=0
        # while left<right:
        #     if height[left]<height[right]:
                
        #         left_max=max(left_max,height[left])
        #         water+=max(0,left_max-height[left])
        #         left+=1
        #     else:
               
        #         right_max=max(right_max,height[right])
        #         water+=max(0,right_max-height[right])
        #         right-=1
        # return water
        total=0
        n=len(height)
        prefix=[0]*n
        prefix[0]=height[0]
        for i in range(1,n-1):
            prefix[i]=max(prefix[i-1],height[i])
        print(prefix)
        suffix=[0]*n
        suffix[n-1]=height[n-1]
        for i in range(n-2,-1,-1):
            suffix[i]=max(suffix[i+1],height[i])
        print(suffix)
        
        for i in range(1,n-1):
            left_max=prefix[i]
            right_max=suffix[i]
            if height[i]<left_max and height[i]<right_max:
                total+=min(left_max,right_max)-height[i]
        return total

