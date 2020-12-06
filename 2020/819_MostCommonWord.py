from collections import Counter, defaultdict


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        punctuations = "!?',;."
        paragraph = paragraph.lower()
        for s in paragraph:
            if s in punctuations:
                paragraph = paragraph.replace(s, " ")

        temp = Counter(paragraph.split())

        tempDict = defaultdict(list)
        for k, v in sorted(temp.items(), key=lambda v: v[1], reverse=True):
            if k not in banned:
                return k
