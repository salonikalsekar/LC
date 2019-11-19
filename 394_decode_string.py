class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for ch in s:
            if ch != "]":
                stack.append(ch)
            else:
                t = []
                while stack and stack[-1] != "[":
                    t.append(stack.pop())
                stack.pop()
                dig = ""
                while stack and stack[-1].isdigit():
                    dig += str(stack.pop())
                stack.append("".join(t[::-1]*int(dig[::-1])))
        return "".join(stack)