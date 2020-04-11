class Solution:
    def maxNumberOfApples(self, arr: List[int]) -> int:
        arr = sorted(arr)
        count = 0
        sumVal = 5000
        for idx, weight in enumerate(arr):
            sumVal -= weight
            if sumVal <= 0:
                return count
            count += 1
        return len(arr)