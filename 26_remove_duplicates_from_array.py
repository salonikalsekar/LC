class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = []
        s = set()
        for n in nums:
            if n not in s:
                l.append(n)
                s.add(n)

        nums[:len(s)] = l

        return len(s)