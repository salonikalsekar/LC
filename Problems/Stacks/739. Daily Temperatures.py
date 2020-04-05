class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        stack = []
        res = [0 for i in range(len(T))]
        for i,t in enumerate(T):
            while len(stack) > 0:
                if stack[-1][0] < t:
                    idx = stack[-1][1]
                    res[idx] = i - idx
                    stack.pop()
                else:
                    break
            stack.append((t,i))
        return res