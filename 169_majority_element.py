class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        temp = set(nums)
        ans = 0
        for i in temp:
            if nums.count(i) > len(nums) // 2:
                return(i)