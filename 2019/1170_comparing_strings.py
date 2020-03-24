import sys

class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        res = []

        query = [i.count(min(i)) for i in queries]
        word = [j.count(min(j)) for j in words]


        for i in query:
            minVal = 0
            for j in word:
                if i < j:
                    minVal +=1


            res.append(minVal)

        return(res)