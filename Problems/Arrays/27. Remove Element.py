class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        temp = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[temp] = nums[i]
                temp += 1
        return temp
