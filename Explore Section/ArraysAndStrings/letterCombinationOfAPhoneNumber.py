class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        combinations = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']

        }
        if not digits:
            return []

        def letterCombinations(comb, dig):
            if len(dig) == 0:
                output.append(comb)
            else:
                for letter in combinations[dig[0]]:
                    letterCombinations(comb + letter, dig[1:])

        output = []
        letterCombinations("", digits)

        return output
