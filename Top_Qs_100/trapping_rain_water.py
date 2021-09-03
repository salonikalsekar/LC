class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft = [0] * len(height)
        maxRight = [0] * len(height)
        minVal = [0] * len(height)

        maxLeft[0] = height[0]
        maxRight[-1] = height[-1]
        l = len(height)

        for i in range(1, l):
            maxLeft[i] = max(height[i], maxLeft[i - 1])

        for i in range(l - 2, -1, -1):
            maxRight[i] = max(height[i], maxRight[i + 1])

        for i in range(l):
            minVal[i] = abs(min(maxLeft[i], maxRight[i]) - height[i])

        return sum(minVal)