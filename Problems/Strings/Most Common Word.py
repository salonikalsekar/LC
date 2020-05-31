from collections import Counter


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        puncList = ['!', '?', "'", ',', ';', '.']

        for i in paragraph:
            if i in puncList:
                paragraph = paragraph.replace(i, " ")
        paragraph = paragraph.lower()
        counter = Counter(paragraph.split())

        for k, v in sorted(counter.items(), key=lambda v: v[1], reverse=True):
            if k not in banned:
                return k.lower()
