import sys
from heapq import heapify, heappush, heappop

class Node:
    def __init__(self, weight):
        self.weight = weight
        self.parent = None
            
    def __lt__(self, other):
        return self.weight < other.weight

class Aggregate(Node):
    def __init__(self, weight, left, right):
        super().__init__(weight)
        self.left = left
        self.right = right
        self.left.parent = self
        self.right.parent = self

class Leaf(Node):
    def __init__(self, symbol, weight):
        super().__init__(weight)
        self.symbol = symbol

class HuffmanTree:
    def __init__(self, weights):
        self.leaves = self.__create_leaves(weights)
        self.root = self.__build_tree() if len(self.leaves) > 0 else None

    def encode(self, data):
        """
        'data' must contains symbols only from the alphabet 'self' instance has been created from
        """
        if type(self.root) is Leaf: # special case of degenerate tree
            return '0' * len(data)
        code = []
        for sym in data:
            code += self.__encode_symbol(sym)
        return ''.join(code)

    def decode(self, code):
        """
        'code' must be a string returned from the 'encode' method invoked on instance of HuffmanTree class
        constructed using the same alphabet 'self' has been instantiated from
        """
        if type(self.root) is Leaf: # special case of degenerate tree
            return self.root.symbol * len(code)
        symbols = []
        index = 0
        while index < len(code):
            curr = self.root
            while type(curr) is not Leaf:
                curr = curr.left if code[index] == '0' else curr.right
                index += 1
            symbols.append(curr.symbol)
        return ''.join(symbols)

    def __encode_symbol(self, sym):
        code = []
        child = self.leaves[sym]
        parent = child.parent
        while parent:
            code.append('0' if parent.left is child else '1')
            child = parent
            parent = parent.parent
        return reversed(code)

    def __create_leaves(self, weights):
        leaves = {}
        for sym, w in weights.items():
            leaves[sym] = Leaf(sym, w)
        return leaves

    def __build_tree(self):
        pqueue = [leaf for _, leaf in self.leaves.items()]
        heapify(pqueue)
        while len(pqueue) > 1:
            l = heappop(pqueue)
            r = heappop(pqueue)
            heappush(pqueue, Aggregate(l.weight + r.weight, l, r))
        return heappop(pqueue)

def get_symbol_weights(data):
    res = {}
    for sym in data:
        res[sym] = res.get(sym, 0) + 1
    return res

def huffman_encoding(data):
    tree = HuffmanTree(get_symbol_weights(data))
    return tree.encode(data), tree

def huffman_decoding(data, tree):
    return tree.decode(data)

def compression_ratio(data, code):
    """
    'data'(str): each character represents 8 bits of information (ASCII symbol)
    'code'(str): each character represents 1 bit of information in Huffman code
    """
    return 8 * len(data) / len(code) if len(code) > 0 else 1

def test(test_id, message):
    code, tree = huffman_encoding(message)
    data = huffman_decoding(code, tree)
    ratio = compression_ratio(message, code)
    print("Test {}".format(test_id))
    print("code = '{}' decoded = '{}' ratio = {:.2f}".format(code, data, ratio))
    print("")

if __name__ == "__main__":
    test_id = 0

    test_id += 1
    test(test_id, "AAA") # Edge case: string with repetitive character
    # Test 1
    # code = '000' decoded = 'AAA' ratio = 8.00

    test_id += 1
    test(test_id, "") # Edge case: empty string
    # Test 2
    # code = '' decoded = '' ratio = 1.00

    test_id += 1
    test(test_id, "Huffman Coding assignment was great!")
    # Test 3
    # code = '110000011110001000000101011110110010100100001100000111111100110101101110100001110111100011011111110100111001101011010111110100101011010101011001' decoded = 'Huffman Coding assignment was great!' ratio = 2.00

