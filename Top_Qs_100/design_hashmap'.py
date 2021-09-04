class Bucket:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.bucket = []

    def update(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        found = False
        for idx, i in enumerate(self.bucket):

            if i[0] == key:
                found = True
                self.bucket[idx] = (key, value)

        if not found:
            self.bucket.append((key, value))

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        for idx, i in enumerate(self.bucket):
            if i[0] == key:
                return i[1]

        return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        for idx, i in enumerate(self.bucket):
            if i[0] == key:
                del self.bucket[idx]


class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.max_num = 2069
        self.hash_map = [Bucket() for x in range(self.max_num)]

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        hashed_key = key % self.max_num
        self.hash_map[hashed_key].update(key, value)

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        hashed_key = key % self.max_num
        return self.hash_map[hashed_key].get(key)

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        hashed_key = key % self.max_num
        self.hash_map[hashed_key].remove(key)

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)