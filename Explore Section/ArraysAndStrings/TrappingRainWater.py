class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        leftMax = []
        rightMax = []
        minimumHeight = []
        for i in range(len(height)):
            leftMax.append(0)
            rightMax.append(0)
            minimumHeight.append(0)

        leftMax[0] = height[0]
        rightMax[len(height) - 1] = height[len(height) - 1]

        for i in range(1, len(height)):
            maxVal = max(leftMax[i - 1], height[i])
            leftMax[i] = maxVal

        for i in range(len(height) - 2, -1, -1):
            maxVal = max(rightMax[i + 1], height[i])
            rightMax[i] = maxVal

        for i in range(len(height)):
            minimumHeight[i] = (min(leftMax[i], rightMax[i])) - height[i]

        return sum(minimumHeight)

