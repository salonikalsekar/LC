class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        current_pointer = "I"
        intVal = 0

        for curr in s[::-1]:

            if dic[curr] < dic[current_pointer]:
                intVal -= dic[curr]
            else:
                intVal += dic[curr]

            current_pointer = curr

        return intVal