import bisect

class MyHashSet:

    def __init__(self):
        self.size = 107
        self.arr = [[] for i in range(self.size)]
        
    def hfn(self, key):
        key = ((key >> 16) ^ key) * 0x45d9f3b
        key = ((key >> 16) ^ key) * 0x45d9f3b
        key = (key >> 16) ^ key
        return key % self.size

    def add(self, key: int) -> None:
        pos = bisect.bisect_left(self.arr[self.hfn(key)], key)
        if pos >= len(self.arr[self.hfn(key)]) or self.arr[self.hfn(key)][pos] != key:
            self.arr[self.hfn(key)].insert(pos, key)

    def remove(self, key: int) -> None:
        pos = bisect.bisect_left(self.arr[self.hfn(key)], key)
        if pos < len(self.arr[self.hfn(key)]) and self.arr[self.hfn(key)][pos] == key:
            del self.arr[self.hfn(key)][pos]

    def contains(self, key: int) -> bool:
        pos = bisect.bisect_left(self.arr[self.hfn(key)], key)
        if pos < len(self.arr[self.hfn(key)]) and self.arr[self.hfn(key)][pos] == key:
            return True
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)