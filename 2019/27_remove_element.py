class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i= 0
        while i < len(nums):
            if nums[i]==val:
                nums.remove(nums[i])
            else:
                i+=1
        return(len(nums))

# class Solution:
#     def removeElement(self, nums: List[int], val: int) -> int:
#        for i in range(nums.count(val)):
#             nums.remove(val)
#        return(len(nums))