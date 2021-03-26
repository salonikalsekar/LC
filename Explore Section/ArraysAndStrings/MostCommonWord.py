from collections import Counter


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        punctuations = "!?',;."
        paragraph = paragraph.lower()

        for i in paragraph:
            if i in punctuations:
                paragraph = paragraph.replace(i, ' ')

        temp = Counter(paragraph.split())
        temp = sorted(temp.items(), key=lambda x: x[1], reverse=True)
        for k, v in temp:
            if k not in banned:
                return k