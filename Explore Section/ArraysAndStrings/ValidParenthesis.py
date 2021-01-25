class Solution:
    def isValid(self, s: str) -> bool:

        brackets = {'}': '{', ']': '[', ')': '('}
        stack = []
        stack.append(s[0])
        for i in s[1:]:
            if i in brackets and stack:
                if brackets[i] == stack[-1]:
                    stack.pop()

                else:
                    stack.append(i)
            else:
                stack.append(i)

        if stack:
            return False

        return True