import os

def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    if os.path.isfile(path):
        return [path] if path.endswith(suffix) else []

    if not os.path.isdir(path):
        return None

    res = []

    def __find_files(suffix, _dir):
        for entry in os.listdir(_dir):
            entry = os.path.join(_dir, entry)

            if os.path.isfile(entry):
                if entry.endswith(suffix):
                    res.append(entry)
                continue

            if os.path.isdir(entry):
                __find_files(suffix, entry)

    __find_files(suffix, path)
    return res

def test(test_id, suffix, path):
    print("Test {}".format(test_id))
    print(find_files(suffix, path))
    print("")

if __name__ == "__main__":
    test_id = 0

    test_id += 1
    test(test_id, ".c", "") # Edge case: empty path
    # Test 1
    # None

    test_id += 1
    test(test_id, ".c", "./testdir/subdir1/a.c") # Edge case: file (not subdirectory) path
    # Test 2
    # ['./testdir/subdir1/a.c']

    test_id += 1
    test(test_id, ".c", "./testdir/subdir1/a.h")
    # Test 3
    # []

    test_id += 1
    test(test_id, ".c", "./testdir/nonexistent_dir") # Edge case: nonexistent subdirectory
    # Test 4
    # None

    test_id += 1
    test(test_id, ".c", "./testdir/subdir4") # Edge case: subdirectory containing no files with specified suffix 
    # Test 5
    # []

    test_id += 1
    test(test_id, ".c", "./testdir/subdir3/subsubdir1")
    # Test 6
    # ['./testdir/subdir3/subsubdir1/b.c']

    test_id += 1
    test(test_id, ".c", "./testdir")
    # Test 7
    # ['./testdir/subdir3/subsubdir1/b.c', './testdir/subdir1/a.c', './testdir/subdir5/a.c', './testdir/t1.c']
