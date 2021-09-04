class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRU_Cache:
    def __init__(self, capacity):
        """ 'capacity' must be a positive integer, otherwise it will be set to 1 """
        self.capacity = capacity if capacity > 0 else 1
        self.values = {}
        self.head = None
        self.tail = None

    def get(self, key):
        """ returns value at the given key, -1 if nonexistent """
        if key not in self.values:
            return -1
        node = self.values[key]
        self.__use(node)
        return node.value

    def set(self, key, value):
        """ sets the value for the given key, removes the oldest item if needed """ 
        if key not in self.values:
            if len(self.values) == self.capacity:
                del self.values[self.head.key]
                self.__unlink(self.head)
            node = Node(key, value)
            self.values[key] = node
            self.__link(node)
        else:
            node = self.values[key]
            node.value = value
            self.__use(node)

    def __use(self, node):
        if node is not self.tail:
            self.__unlink(node)
            self.__link(node)

    def __link(self, node):
        if not self.tail:
            self.tail = node
            self.head = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node

    def __unlink(self, node):
        if node is self.head:
            self.head = self.head.next
            if not self.head:
                self.tail = None
            else:
                self.head.prev = None
        elif node is self.tail:
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
        node.prev = None
        node.next = None

def test(test_id, capacity, requests):
    print("Test {}".format(test_id))

    cache = LRU_Cache(capacity)
    for r in requests:
        if type(r) is tuple:
            cache.set(*r)
        else:
            print(cache.get(r))

    print("")

if __name__ == "__main__":
    test_id = 0

    test_id += 1
    test(test_id, 5, [1]) # Edge case: request data from empty cache
    # Test 1
    # -1

    test_id += 1
    test(test_id, 5, [1, (1, 1), 1])
    # Test 2
    # -1
    # 1

    test_id += 1
    test(test_id, 0, [(1, 1), 1, (2, 2), 1, 2]) # Edge case: zero capacity
    # Test 3
    # 1
    # -1
    # 2
    
    test_id += 1
    test(test_id, -1, [(1, 1), 1, (2, 2), 1, 2]) # Edge case: negative capacity
    # Test 4
    # 1
    # -1
    # 2

    test_id += 1
    test(test_id, 2, [(1, 1), (2, 2), (3, 3), (4, 4), 2])
    # Test 5
    # -1

    test_id += 1
    test(test_id, 5, [(1, 1), (2, 2), (3, 3), (4, 4), 1, 2, 100, (5, 5), (6, 6), 3])
    # Test 6
    # 1
    # 2
    # -1
    # -1

