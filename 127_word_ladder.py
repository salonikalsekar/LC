from collections import defaultdict, deque


class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):

        length = len(beginWord)
        d = defaultdict(list)
        if not beginWord or not endWord or not wordList or endWord not in wordList:
            return 0

        for word in wordList:
            for i in range(length):
                d[word[:i] + "*" + word[i + 1:]].append(word)

        q = deque([(beginWord, 1)])
        seen = {beginWord: True}

        while q:
            curr_word, level = q.popleft()

            for i in range(length):

                temp = curr_word[:i] + "*" + curr_word[i + 1:]
                for intermediateWord in d[temp]:
                    if intermediateWord == endWord:
                        return level + 1

                    if intermediateWord not in seen:
                        seen[intermediateWord] = True
                        q.append((intermediateWord, level + 1))

        return 0

