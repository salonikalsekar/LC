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
Solution 4 - heaps O(nlogk)

import heapq as h
class Solution:
    def topKFrequent(self, arr: List[int], k: int) -> List[int]:
        # Make counter dictionary
        count_dict = Counter(arr)
        items = []
        # Revert the key, value order since tuple is sorted by first value in heap
        for key,val in count_dict.items():
            items.append((val,key))
        heap = []
        # push first k elements in heap
        for i in range(k):
            h.heappush(heap,items[i])
        # Push rest of elements by maintaing length = k
        for i in range(k, len(items)):
            
            if items[i][0] >= heap[0][0]:
                h.heappop(heap)
                h.heappush(heap, items[i])
        # Return the values of the tuples
        return [x[1] for x in heap]
