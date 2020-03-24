class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        maxlength = 0

        visited = set()
        setnums = set(nums)

        for i in nums:

            lengthright = 0
            lengthleft = 0

            if i not in visited:
                visited.add(i)

                temp_left = i - 1
                temp_right = i + 1

                while temp_left in setnums:
                    visited.add(temp_left)
                    lengthleft = i - temp_left
                    temp_left -= 1

                while temp_right in setnums:
                    visited.add(temp_right)
                    lengthright = temp_right - i
                    temp_right += 1

            maxlength = max(maxlength, lengthright + lengthleft + 1)

        return maxlength





