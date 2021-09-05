class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone = {

            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']

        }
        output = []

        def createComb(comb, digits, output):

            if not digits:
                output.append(comb)

            else:
                for i in phone[digits[0]]:
                    createComb(comb + i, digits[1:], output)

        if digits:
            createComb("", digits, output)
        return output