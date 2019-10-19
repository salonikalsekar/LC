class Solution:
    def removeVowels(self, S: str) -> str:
        s = ""
        vowels = ('a', 'e', 'i', 'o', 'u')

        for ch in S:
            if ch not in vowels:
                s += ch

        return (s)