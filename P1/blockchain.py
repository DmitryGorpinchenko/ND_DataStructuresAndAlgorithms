import datetime
import hashlib

class Block:
    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()
        self.next = None

    def calc_hash(self):
        hash_str = str(self.timestamp)
        hash_str += str(self.data)
        hash_str += self.previous_hash
        
        sha = hashlib.sha256()
        sha.update(hash_str.encode('utf-8'))
        return sha.hexdigest()

    def __repr__(self):
        res = '{\n    "Timestamp": "'
        res += str(self.timestamp)
        res += '",\n    "Data": "'
        res += str(self.data)
        res += '",\n    "Previous Hash": '
        res += self.previous_hash
        res += ',\n    "Hash": '
        res += self.hash
        res += '\n}'
        return res

class Blockchain:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_block(self, timestamp, data):
        if not data:
            return
        if not self.tail:
            block = Block(timestamp, data, "0")
            self.tail = block
            self.head = block
        else:
            block = Block(timestamp, data, self.tail.hash)
            self.tail.next = block
            self.tail = block

    def is_valid(self):
        if not self.head:
            return True
        if self.head.calc_hash() != self.head.hash:
            return False

        prev = self.head
        curr = prev.next
        while curr:
            if curr.calc_hash() != curr.hash:
                return False
            if prev.hash != curr.previous_hash:
                return False
            prev = curr
            curr = curr.next

        return True

    def __str__(self):
        res = '['
        curr = self.head
        while curr:
            if curr is not self.head:
                res += ','
                res += '\n'
            res += str(curr)
            curr = curr.next
        res += ']'
        return res

def create_blockchain(data):
    res = Blockchain()
    for d in data:
        res.add_block(datetime.datetime.utcnow(), d)
    return res

def test(test_id, blockchain):
    print("Test {}".format(test_id))
    print(blockchain)
    print("")

if __name__ == "__main__":
    test_id = 0

    test_id += 1
    test(test_id, create_blockchain([])) # Edge case: empty chain
    # Test 1
    # []

    test_id += 1
    test(test_id, create_blockchain([""])) # Edge case: block with empty data
    # Test 2
    # []

    test_id += 1
    test(test_id, create_blockchain([None])) # Edge case: block with None data
    # Test 3
    # []

    # NOTE: test output below may vary depending on UTC time at the moment of program launch

    test_id += 1
    test(test_id, create_blockchain(["data", "data", "other_data"])) # chain containing 3 blocks
    # Test 4
    # [{
    #     "Timestamp": "2021-09-07 10:28:22.315230",
    #     "Data": "data",
    #     "Previous Hash": 0,
    #     "Hash": 9e6185f6066add05a88588dccfe3a69fba8a641d9edb4ce99e4230d19b246006
    # },
    # {
    #     "Timestamp": "2021-09-07 10:28:22.315245",
    #     "Data": "data",
    #     "Previous Hash": 9e6185f6066add05a88588dccfe3a69fba8a641d9edb4ce99e4230d19b246006,
    #     "Hash": 30aa7b6aa063007ee6999c62069eb7e1b215c765dd7f5e1c7f0d6a282dc4d2d9
    # },
    # {
    #     "Timestamp": "2021-09-07 10:28:22.315250",
    #     "Data": "other_data",
    #     "Previous Hash": 30aa7b6aa063007ee6999c62069eb7e1b215c765dd7f5e1c7f0d6a282dc4d2d9,
    #     "Hash": 26efe70da0286ad1f48ba5aea7e9e1837762e3a0922467b9fe3eae4e63dddc28
    # }]

