def swap(arr, i, j):
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp

def partition_3way(arr, pivot):
    """
    this is an adoptation of the famous Dijkstra's 3-way partitioning algorithm
    used to speed up quicksort for arrays with many duplicate elements
    """
    l = 0
    r = len(arr)
    i = 0
    while i < r:
        if arr[i] < pivot:
            swap(arr, l, i)
            l += 1
            i += 1
        elif arr[i] > pivot:
            r -= 1
            swap(arr, i, r)
        else:
            i += 1

def sort_012(arr):
    """
    sorts the array consisting of only 0, 1, and 2 in a single traversal
    """
    partition_3way(arr, 1)

def test(test_id, test_case):
    if test_id > 1:
        print("")
    print("Test {}".format(test_id))
    sol = sorted(test_case)
    sort_012(test_case)
    print(test_case)
    print("Pass" if test_case == sol else "Fail")

if __name__ == "__main__":
    test_id = 0

    test_id += 1
    test(test_id, []) # Edge case: empty array
    # Test 1
    # []
    # Pass

    test_id += 1
    test(test_id, [1, 1, 1, 1, 1, 1, 1]) # Edge case: array consisting only of 1's
    # Test 2
    # [1, 1, 1, 1, 1, 1, 1]
    # Pass

    test_id += 1
    test(test_id, [0, 0, 0, 1, 1, 2, 2, 2, 2]) # Edge case: already sorted array
    # Test 3
    # [0, 0, 0, 1, 1, 2, 2, 2, 2]
    # Pass

    test_id += 1
    test(test_id, [2, 2, 2, 0, 0, 0, 0]) # Edge case: array consisting only of 0's and 2's in descending order
    # Test 4
    # [0, 0, 0, 0, 2, 2, 2]
    # Pass

    test_id += 1
    test(test_id, [0, 1, 0, 1, 0, 1, 2, 1, 0, 2])
    # Test 5
    # [0, 0, 0, 0, 1, 1, 1, 1, 2, 2]
    # Pass

