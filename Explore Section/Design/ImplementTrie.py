class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hm = {}

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        cur = self.hm
        for w in word:
            if w not in cur:
                cur[w] = {}
            cur = cur[w]
        cur['#'] = ''

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        cur = self.hm
        for w in word:
            if w not in cur:
                return False

            cur = cur[w]
        return '#' in cur

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        cur = self.hm
        for p in prefix:
            if p not in cur:
                return False
            cur = cur[p]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)