class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.num_elements = 0

    def append(self, value):
        node = Node(value)
        if not self.tail:
            self.tail = node
            self.head = node
        else:
            self.tail.next = node
            self.tail = node
        self.num_elements += 1

    def size(self):
        return self.num_elements

    def __str__(self):
        res = ""
        curr = self.head
        while curr:
            res += str(curr) + " -> "
            curr = curr.next
        return res

    def __iter__(self):
        curr = self.head
        while curr:
            yield curr.value
            curr = curr.next

def to_llist(iterable):
    res = LinkedList()
    for el in iterable:
        res.append(el)
    return res

def to_list(llist):
    res = []
    for el in llist:
        res.append(el)
    return res

def to_sorted_llist(llist):
    return to_llist(sorted(to_list(llist)))

def to_set(llist):
    res = set()
    for el in llist:
        res.add(el)
    return res

def union(llist_1, llist_2):
    union_set = set()
    for el in llist_1:
        union_set.add(el)
    for el in llist_2:
        union_set.add(el)
    return to_llist(union_set)

def intersection(llist_1, llist_2):
    intersection_set = set()

    if llist_2.size() > llist_1.size():
        llist_1, llist_2 = llist_2, llist_1

    set_2 = to_set(llist_2)
    for el in llist_1:
        if el in set_2:
            intersection_set.add(el)
    return to_llist(intersection_set)

def test(test_id, list_1, list_2):
    llist_1 = to_llist(list_1)
    llist_2 = to_llist(list_2)
    print("Test {}".format(test_id))
    print("union: '{}'".format(to_sorted_llist(union(llist_1, llist_2))))
    print("intersection '{}'".format(to_sorted_llist(intersection(llist_1, llist_2))))
    print("")

if __name__ == "__main__":
    test_id = 0

    test_id += 1
    test(test_id, [], []) # Edge case: both lists are empty 
    # Test 1
    # union: ''
    # intersection ''

    test_id += 1
    test(test_id, [], [1, 2, 3]) # Edge case: first list is empty 
    # Test 2
    # union: '1 -> 2 -> 3 -> '
    # intersection ''

    test_id += 1
    test(test_id, [1, 2, 3], [4, 5, 6])
    # Test 3
    # union: '1 -> 2 -> 3 -> 4 -> 5 -> 6 -> '
    # intersection ''

    test_id += 1
    test(test_id, [7, 8, 9], [7, 8, 9])
    # Test 4
    # union: '7 -> 8 -> 9 -> '
    # intersection '7 -> 8 -> 9 -> '

    test_id += 1
    test(test_id, [7, 7, 8, 9, 9, 9], [11, 9, 10, 11])
    # Test 5
    # union: '7 -> 8 -> 9 -> 10 -> 11 -> '
    # intersection '9 -> '

