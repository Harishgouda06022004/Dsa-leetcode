class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area=0
       
        left=0
        right=len(height)-1
        while left<=right:
            Area=min(height[left],height[right])*(right-left)
            max_area=max(max_area,Area)
            if height[left]<height[right]:
                left+=1
            elif height[left]>=height[right]:
                right-=1
        return max_area