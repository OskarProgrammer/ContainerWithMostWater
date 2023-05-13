class Solution:
    def maxArea(self, height: List[int]) -> int:
        left=0
        right = len(height)-1
        result = 0
        while left<=right:
            pole=min(height[right],height[left])*(right-left)
            result=max(result,pole)
            if height[right]>height[left]:
                left+=1
            else:
                right-=1
        return result