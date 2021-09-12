def rotated_array_search(arr, target):
    """
    returns index of 'target' in the rotated sorted array 'arr' or -1 if not found
    """
    lo = 0
    hi = len(arr)
    while lo < hi:
        m = lo + (hi - lo)//2
        if arr[m] == target:
            return m
        if arr[m] < target:
            if (arr[lo] <= arr[m]) or (arr[hi - 1] >= target):
                lo = m + 1
            else:
                hi = m
        else:
            if (arr[hi - 1] >= arr[m]) or (arr[lo] <= target):
                hi = m
            else:
                lo = m + 1
    return -1

def test(test_id, test_case):
    def __linear_search(input_list, number):
        for index, element in enumerate(input_list):
            if element == number:
                return index
        return -1

    if test_id > 1:
        print("")
    print("Test {}".format(test_id))
    index = rotated_array_search(test_case[0], test_case[1])
    print(index)
    print("Pass" if index == __linear_search(test_case[0], test_case[1]) else "Fail")

if __name__ == "__main__":
    test_id = 0

    test_id += 1
    test(test_id, ([], 1)) # Edge case: empty array
    # Test 1
    # -1
    # Pass

    test_id += 1
    test(test_id, ([1, 2, 3, 4, 5, 6], 3)) # Edge case: not rotated array
    # Test 2
    # 2
    # Pass

    test_id += 1
    test(test_id, ([6, 7, 8, 9, 1, 2, 3, 4], 6)) # Edge case: target equals to first element
    # Test 3
    # 0
    # Pass

    test_id += 1
    test(test_id, ([6, 7, 8, 9, 1, 2, 3, 4], 4)) # Edge case: target equals to last element
    # Test 4
    # 7
    # Pass

    test_id += 1
    test(test_id, ([6, 7, 8, 1, 2, 3, 4, 5], 8)) # Edge case: target equals to max element
    # Test 5
    # 2
    # Pass

    test_id += 1
    test(test_id, ([6, 7, 8, 1, 2, 3, 4, 5], 1)) # Edge case: target equals to min element
    # Test 6
    # 3
    # Pass

    test_id += 1
    test(test_id, ([7, 8, 9, 1, 2, 3, 4, 5, 6], 0)) # Edge case: non-existing target
    # Test 7
    # -1
    # Pass

    test_id += 1
    test(test_id, ([7, 8, 9, 1, 2, 3, 4, 5, 6], 7))
    # Test 8
    # 0
    # Pass

    test_id += 1
    test(test_id, ([7, 8, 9, 1, 2, 3, 4, 5, 6], 8))
    # Test 9
    # 1
    # Pass

    test_id += 1
    test(test_id, ([7, 8, 9, 1, 2, 3, 4, 5, 6], 9))
    # Test 10
    # 2
    # Pass

    test_id += 1
    test(test_id, ([7, 8, 9, 1, 2, 3, 4, 5, 6], 1))
    # Test 11
    # 3
    # Pass

    test_id += 1
    test(test_id, ([7, 8, 9, 1, 2, 3, 4, 5, 6], 2))
    # Test 12
    # 4
    # Pass

    test_id += 1
    test(test_id, ([7, 8, 9, 1, 2, 3, 4, 5, 6], 3))
    # Test 13
    # 5
    # Pass

    test_id += 1
    test(test_id, ([7, 8, 9, 1, 2, 3, 4, 5, 6], 4))
    # Test 14
    # 6
    # Pass

    test_id += 1
    test(test_id, ([7, 8, 9, 1, 2, 3, 4, 5, 6], 5))
    # Test 15
    # 7
    # Pass

    test_id += 1
    test(test_id, ([7, 8, 9, 1, 2, 3, 4, 5, 6], 6))
    # Test 16
    # 8
    # Pass
