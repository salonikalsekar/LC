class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.s = set()

    def add(self, key: int) -> None:
        if key not in self.s:
            self.s.add(key)

    def remove(self, key: int) -> None:
        if key in self.s:
            self.s.remove(key)

        return self.s

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        if key in self.s:
            return True
        return False

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)