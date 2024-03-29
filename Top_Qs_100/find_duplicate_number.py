class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for num in nums:
            cur = abs(num)

            if nums[cur] < 0:
                duplicate = cur
                break

            nums[cur] = -nums[cur]

        for n in nums:
            nums[n] = abs(nums[n])

        return duplicate