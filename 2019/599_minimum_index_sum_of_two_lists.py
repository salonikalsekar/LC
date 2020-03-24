from collections import defaultdict


class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        temp = defaultdict(list)
        res = []
        for i in range(len(list1)):
            if list1[i] in list2:
                temp[i + list2.index(list1[i])].append(list1[i])

        return temp[min(temp)]
