class Solution:
    def compress(self, chars: List[str]) -> int:
        w = 0
        anch = 0
        for read, ch in enumerate(chars):
            if read + 1 == len(chars) or chars[read + 1] != ch:
                chars[w] = chars[anch]
                w += 1
                if read > anch:
                    for i in str(read - anch + 1):
                        chars[w] = i
                        w += 1
                anch = read + 1

        return w

