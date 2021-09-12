def rearrange_digits(digits):
    counts = [0 for _ in range(10)]
    for d in digits:
        counts[d] += 1

    upper_bound = 10

    def __extract_max_digit():
        for i in range(upper_bound):
            d = upper_bound - 1 - i
            if counts[d] > 0:
                counts[d] -= 1
                return d
        return None

    num1 = 0
    num2 = 0

    while True:
        d1 = __extract_max_digit()
        if d1 is None:
            break

        num1 *= 10
        num1 += d1
        upper_bound = d1 + 1

        d2 = __extract_max_digit()
        if d2 is None:
            break

        num2 *= 10
        num2 += d2
        upper_bound = d2 + 1
    
    return [num1, num2]

def test(test_id, test_case):
    if test_id > 1:
        print("")
    print("Test {}".format(test_id))
    nums = rearrange_digits(test_case[0])
    print(nums)
    print("Pass" if sum(nums) == test_case[1] else "Fail")

if __name__ == "__main__":
    test_id = 0

    test_id += 1
    test(test_id, ([], 0)) # Edge case: empty input
    # Test 1
    # [0, 0]
    # Pass

    test_id += 1
    test(test_id, ([3], 3)) # Edge case: single digit
    # Test 2
    # [3, 0]
    # Pass

    test_id += 1
    test(test_id, ([0, 0, 0, 0, 0, 0, 0], 0)) # Edge case: all zeros
    # Test 3
    # [0, 0]
    # Pass

    test_id += 1
    test(test_id, ([1, 2, 3, 1, 2, 3], sum([321, 321])))
    # Test 4
    # [321, 321]
    # Pass

    test_id += 1
    test(test_id, ([7, 3, 2, 6, 4, 5, 1], sum([7531, 642])))
    # Test 5
    # [7531, 642]
    # Pass

