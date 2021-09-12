class RouteTrieNode:
    def __init__(self, handler=None):
        self.handler = handler
        self.children = {}

    def insert(self, route_part):
        if route_part not in self.children:
            self.children[route_part] = RouteTrieNode()
        return self.children[route_part]

class RouteTrie:
    def __init__(self, root_handler):
        self.root = RouteTrieNode(root_handler)

    def insert(self, route, handler):
        """
        empty 'route' list corresponds to the root
        """
        curr = self.root
        for part in route:
            curr = curr.insert(part)
        curr.handler = handler

    def find(self, route):
        """
        empty 'route' list corresponds to the root
        """
        curr = self.root
        for part in route:
            if part not in curr.children:
                return None
            curr = curr.children[part]
        return curr.handler

class Router:
    def __init__(self, root_handler):
        self.trie = RouteTrie(root_handler)

    def add_handler(self, path, handler):
        self.trie.insert(self.split_path(path), handler)

    def lookup(self, path):
        return self.trie.find(self.split_path(path))

    def split_path(self, path):
        """
        returns parts of the route as list

        NOTE: empty list is returned if 'path' corresponds to the root
        """
        path = path.strip("/")
        return path.split("/") if len(path) > 0 else []

def test(test_id, test_case):
    if test_id > 1:
        print("")
    print("Test {}".format(test_id))
    paths, path, sol = test_case
    router = Router("root handler")
    for p in paths:
        router.add_handler(*p)
    res = router.lookup(path)
    print(res)
    print("Pass" if res == sol else "Fail")

if __name__ == "__main__":
    test_id = 0

    paths = [("/home/page1", "page1 handler"), ("/home/page2", "page2 handler")]

    test_id += 1
    test(test_id, (paths, "", "root handler")) # Edge case: root as empty path
    # Test 1
    # root handler
    # Pass
    
    test_id += 1
    test(test_id, (paths, "/", "root handler"))
    # Test 2
    # root handler
    # Pass
    
    test_id += 1
    test(test_id, ([], "/", "root handler")) # Edge case: empty paths list
    # Test 3
    # root handler
    # Pass
    
    test_id += 1
    test(test_id, ([], "/home", None))
    # Test 4
    # None
    # Pass

    test_id += 1
    test(test_id, (paths, "/home", None)) # Edge case: incomplete path lookup
    # Test 5
    # None
    # Pass

    test_id += 1
    test(test_id, (paths, "/home/page1/", "page1 handler")) # Edge case: trailing slash
    # Test 6
    # page1 handler
    # Pass
    
    test_id += 1
    test(test_id, (paths, "/home/page1", "page1 handler"))
    # Test 7
    # page1 handler
    # Pass

    test_id += 1
    test(test_id, (paths, "/home/page2/subpage2", None))
    # Test 8
    # None
    # Pass

