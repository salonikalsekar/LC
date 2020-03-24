class Solution:
    def myAtoi(self, str: str) -> int:

        num = ""
        str = str.lstrip(" ")

        if not str:
            return 0

        if str[0] in ["-", "+"]:
            num = str[0]
            str = str[1:]

        for ch in str:
            if ch.isdigit():
                num += ch
            else:
                break

        try:
            value = int(num)

            if (value.bit_length() >= 32):
                return (2 ** 31 - 1) if value > 0 else -2 ** 31
            return value
        except ValueError:
            return 0
