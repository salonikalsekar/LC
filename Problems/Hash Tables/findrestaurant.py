class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        res = []

        h = {}
        h1 = {}

        for idx, i in enumerate(list1):
            h[i] = idx

        minVal = float('inf')

        for idx, i in enumerate(list2):
            if i in h:

                if minVal > h[i] + idx:
                    minVal = h[i] + idx
                    res = [i]
                elif minVal == h[i] + idx:
                    res.append(i)

        return res
