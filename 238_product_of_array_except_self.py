class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        prod_zero = 1
        final = []
        nums1 = list(filter(lambda a: a != 0, nums))
        countZero = nums.count(0)
        for j in nums1:
            prod *= j

        for num in nums:
            if num != 0:
                if countZero == 0:
                    final.append(prod // num)
                else:
                    final.append(0)

            else:
                if countZero > 1:
                    final.append(0)
                else:
                    final.append(prod)

        return (final)