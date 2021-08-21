class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        temp = {
            ']': '[',
            '}': '{',
            ')': '('
        }
        for p in s:
            if p in temp:
                if stack and stack[-1] == temp[p]:
                    stack.pop()
                else:
                    stack.append(p)
            else:
                stack.append(p)

        if len(stack) != 0:
            return False

        return True
