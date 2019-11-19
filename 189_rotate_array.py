class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        l = len(nums)
        k = k % l
        nums.reverse()
        nums[k:], nums[:k] = nums[k:][::-1], nums[:k][::-1]