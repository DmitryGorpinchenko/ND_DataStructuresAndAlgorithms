import random

def get_min_max(ints):
    """
    returns a tuple containing minimum and maximum integer from the input data stream
    """
    min_res = None
    max_res = None

    for i in ints:
        if (min_res is None) or (i < min_res):
            min_res = i
        if (max_res is None) or (i > max_res):
            max_res = i

    return min_res, max_res

def test(test_id, ints):
    if test_id > 1:
        print("")
    print("Test {}".format(test_id))
    min_max = get_min_max(ints)
    print(min_max)
    print("Pass" if (min_max == (None, None) and len(ints) == 0) or ((min(ints), max(ints)) == min_max) else "Fail")

if __name__ == "__main__":
    test_id = 0

    test_id += 1
    test(test_id, []) # Edge case: empty input stream
    # Test 1
    # (None, None)
    # Pass

    test_id += 1
    test(test_id, [7]) # Edge case: single integer list, min and max are the same
    # Test 2
    # (7, 7)
    # Pass

    large_list = [i for i in range(0, 1000000)]
    random.shuffle(large_list)
    test_id += 1
    test(test_id, large_list) # Edge case: large randomized input
    # Test 3
    # (0, 999999)
    # Pass
    
    test_id += 1
    test(test_id, [10, 9, 8, 7, 6, 5, 4, 3])
    # Test 4
    # (3, 10)
    # Pass

