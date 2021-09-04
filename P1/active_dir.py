class Group:
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = set()

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.add(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name

def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    visited = set()

    def __is_user_in_group(user, group):
        if group in visited:
            return False

        if user in group.get_users():
            return True
        for sub_group in group.get_groups():
            if __is_user_in_group(user, sub_group):
                return True

        visited.add(group)
        return False

    return __is_user_in_group(user, group)

def generate_graph(n, user):
    res = Group("large graph")

    stump = Group("stump")
    for _ in range(n):
        group = Group("")
        stump.add_group(group)

    for i in range(n):
        group = Group("")
        group.add_group(stump)
        res.add_group(group)

    if user:
        user_group = Group("")
        user_group.add_user(user)
        res.add_group(user_group)

    return res

def create_small_group(user):
    parent = Group("parent")
    child1 = Group("child1")
    child2 = Group("child2")
    child2.add_user(user)
    parent.add_group(child1)
    parent.add_group(child2)
    return parent

def test(test_id, user, group):
    print("Test {}".format(test_id))
    print(is_user_in_group(user, group))
    print("")

if __name__ == "__main__":
    test_id = 0

    test_id += 1
    test(test_id, "user", Group("empty group")) # Edge case: empty group
    # Test 1
    # False

    test_id += 1
    test(test_id, "", create_small_group("user")) # Edge case: empty user id
    # Test 2
    # False

    test_id += 1
    test(test_id, "other_user", create_small_group("other_user"))
    # Test 3
    # True

    # tests below demonstrate that caching of already visited groups might drastically speed up search on very large active directory graph structures
    large_graph = generate_graph(100000, "user")

    test_id += 1
    test(test_id, "user", large_graph) # Edge case: large graph
    # Test 4
    # True

    test_id += 1
    test(test_id, "nonexistent_user", large_graph)
    # Test 5
    # False

    test_id += 1
    test(test_id, "user", generate_graph(10000, None))
    # Test 6
    # False

