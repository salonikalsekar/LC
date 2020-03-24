class Solution:
    def isValid(self, s: str) -> bool:
        d = {")": "(", "}": "{", "]": "["}
        stack = []

        for ch in s:
            if ch in d.keys():
                if not stack:
                    return False
                top = stack.pop()
                if top != d[ch]:
                    return False

            if ch in d.values():
                stack.append(ch)

        if stack:
            return False
        else:
            return True
