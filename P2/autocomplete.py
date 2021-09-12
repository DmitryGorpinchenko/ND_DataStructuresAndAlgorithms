class TrieNode:
    def __init__(self):
        self.is_word = False
        self.children = {}

    def insert(self, char):
        if char not in self.children:
            self.children[char] = TrieNode()
        return self.children[char]

    def suffixes(self):
        res = []

        def __suffixes(node, suffix = []):
            for c in node.children:
                suffix.append(c)
                if node.children[c].is_word:
                    res.append(''.join(suffix))
                __suffixes(node.children[c], suffix)
                suffix.pop()

        __suffixes(self)
        return res

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root
        for c in word:
            curr = curr.insert(c)
        curr.is_word = True

    def find(self, prefix):
        curr = self.root
        for c in prefix:
            if c not in curr.children:
                return None
            curr = curr.children[c]
        return curr

    def suffixes(self, prefix):
        node = self.find(prefix)
        return node.suffixes() if node else []

def test(test_id, test_case):
    if test_id > 1:
        print("")
    print("Test {}".format(test_id))
    trie = Trie()
    for w in test_case[0]:
        trie.insert(w)
    suffixes = sorted(trie.suffixes(test_case[1]))
    print(suffixes)
    print("Pass" if suffixes == sorted(test_case[2]) else "Fail")

if __name__ == "__main__":
    test_id = 0

    words = [
        "autopilot", "autobiography", "automobile", "autofocus",
        "deactivate", "debug", "deduce",
        "transmit", "transaction", "translation", "transfer"
    ]

    test_id += 1
    test(test_id, ([], "prefix", [])) # Edge case: empty words list
    # Test 1
    # []
    # Pass

    test_id += 1
    test(test_id, (words, "", words)) # Edge case: empty prefix
    # Test 2
    # ['autobiography', 'autofocus', 'automobile', 'autopilot', 'deactivate', 'debug', 'deduce', 'transaction', 'transfer', 'translation', 'transmit']
    # Pass

    test_id += 1
    test(test_id, (words, "fun", [])) # Edge case: non-existing prefix
    # Test 3
    # []
    # Pass

    test_id += 1
    test(test_id, (words, "trans", ["action", "fer", "lation", "mit"]))
    # Test 4
    # ['action', 'fer', 'lation', 'mit']
    # Pass

    test_id += 1
    test(test_id, (words, "de", ["activate", "bug", "duce"]))
    # Test 5
    # ['activate', 'bug', 'duce']
    # Pass

    test_id += 1
    test(test_id, (words, "au", ["tobiography", "tofocus", "tomobile", "topilot"]))
    # Test 6
    # ['tobiography', 'tofocus', 'tomobile', 'topilot']
    # Pass

