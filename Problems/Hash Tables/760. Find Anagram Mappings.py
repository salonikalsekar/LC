class Solution:
    def anagramMappings(self, A: List[int], B: List[int]) -> List[int]:
        temp = { v: idx for idx, v in enumerate(B) }
        return [temp[x] for x in A]