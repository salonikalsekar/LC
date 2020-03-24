class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        l = 0
        r = len(height) - 1
        maxVal = 0
        while l<r:
            
            h = min(height[l], height[r])
            area = h * (r - l)
            maxVal = max(area, maxVal)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        
        return(maxVal)