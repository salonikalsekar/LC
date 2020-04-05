class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        stack = []
        res = {}
        for i, t in enumerate(T):
            while len(stack) > 0:
                if stack[-1] < t:
                    idx = T.index(stack[-1])
                    res[idx] = i - idx
                    stack.pop()
                else:
                    break
            stack.append(t)

        if stack:
            for i in stack:
                res[T.index(stack[-1])] = 0
        print(res)

