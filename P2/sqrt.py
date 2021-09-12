def sqrt(number):
    """
    returns floor of a square root of the given number
    """
    if number < 0:
        return None

    sqrt_floor = 0

    lo = 0
    hi = number + 1
    while lo < hi:
        m = lo + (hi - lo)//2
        sq = m * m
        if sq == number:
            return m
        if sq > number:
            hi = m
        else:
            sqrt_floor = m
            lo = m + 1

    return sqrt_floor
            

def test(test_id, test_case):
    if test_id > 1:
        print("")
    print("Test {}".format(test_id))
    res = sqrt(test_case[0])
    print("floor(sqrt({}))".format(test_case[0]), "=", res)
    print("Pass" if test_case[1] == res else "Fail")

if __name__ == "__main__":
    test_id = 0

    test_id += 1
    test(test_id, (-1, None)) # Edge case: negative input
    # Test 1
    # floor(sqrt(-1)) = None
    # Pass

    test_id += 1
    test(test_id, (0, 0)) # Edge case: 'zero' input
    # Test 2
    # floor(sqrt(0)) = 0
    # Pass

    test_id += 1
    test(test_id, (1, 1)) # Edge case: 'one' input
    # Test 3
    # floor(sqrt(1)) = 1
    # Pass

    test_id += 1
    test(test_id, (121, 11)) # Edge case: exact integer square root
    # Test 4
    # floor(sqrt(121)) = 11
    # Pass

    test_id += 1
    test(test_id, (37, 6))
    # Test 5
    # floor(sqrt(37)) = 6
    # Pass

