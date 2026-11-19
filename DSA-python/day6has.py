class HashMap:
    """A simple hash map implementation using separate chaining."""

    def __init__(self, size=10):
        self.size = size
        self.buckets = [[] for _ in range(size)]

    def _hash(self, key):
        return hash(key) % self.size

    def put(self, key, value):
        bucket = self.buckets[self._hash(key)]
        for index, (stored_key, _) in enumerate(bucket):
            if stored_key == key:
                bucket[index] = (key, value)
                return
        bucket.append((key, value))

    def get(self, key, default=None):
        bucket = self.buckets[self._hash(key)]
        for stored_key, value in bucket:
            if stored_key == key:
                return value
        return default

    def remove(self, key):
        bucket = self.buckets[self._hash(key)]
        for index, (stored_key, _) in enumerate(bucket):
            if stored_key == key:
                del bucket[index]
                return True
        return False

    def __contains__(self, key):
        return self.get(key) is not None


if __name__ == "__main__":
    hash_map = HashMap()
    hash_map.put("name", "Python")
    hash_map.put("day", 6)

    print(hash_map.get("name"))
    print(hash_map.get("day"))
