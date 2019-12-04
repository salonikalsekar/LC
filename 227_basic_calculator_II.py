class Solution:
    def calculate(self, s):
        op = "+"
        num = 0
        stack = []
        s += '+'

        for c in s:

            if c.isdigit():
                num = num * 10 + int(c)

            elif c == ' ':
                continue

            else:
                if op == '+':
                    stack.append(num)
                elif op == '-':
                    stack.append(-num)
                elif op == '*':
                    temp = stack.pop()
                    stack.append(temp * num)
                elif op == '/':
                    temp = stack.pop()
                    stack.append(math.trunc(temp / num))
                num = 0
                op = c

        return sum(stack)