Solution 1

# from collections import defaultdict

# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:

#         res = []
#         dicttemp = defaultdict(list)
#         settemp = set(nums)

#         for i in settemp:
#             c = nums.count(i)
#             dicttemp[c].append(i)

#         for key,v in sorted(dicttemp.items(), reverse=True):
#             if len(res) == k:
#                 return res

#             if len(res) < k:
#                 if len(v) > 1:
#                     for i in v:
#                         if len(res) < k:
#                             res.append(i)
#                 else:
#                     res.append(v[0])

#         return res
Solution 2
from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c_dict = Counter(nums)

        return sorted(c_dict.keys(), key=c_dict.get, reverse=True)[:k]





---------------------------------------
Solution 3
Using heaps - nlogn

from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        
        q = []
        
        for key, value in c.items():
            heapq.heappush(q, (-1 * value, key))
                 
        return [heappop(q)[1] for _ in range(k)]

-------------------------------------------------------------------------------------------------------------------------
Solution 4 - heaps time - O(nlogk) 
space - O(N + k) for N length array and k length heap

import heapq
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        1. Create frequency hashmap to accumulate counts by element
        2. Use heap data structure, such that for each element in the array
            .heappushpop(element) when k == len(nums)
            .heappush(element) otherwise
        3. Return a list of k elements (without frequency values)
        '''

        d_freq = Counter(nums)
        
        heap = []
        for num, freq in d_freq.items():
            if k == len(heap):
                heapq.heappushpop(heap, (freq, num))
            else:
                heapq.heappush(heap, (freq, num))
                
                
        res = []
        for freq, num in heap:
            res.append(num)
            
        return res
