## Square Root of an Integer (sqrt.py)
* N - given integer number
* Time Complexity: O(log(N))
* Space Complexity: O(1)

Problem is solved by using a variation/extention of binary search algorithm (hence, time complexity is logarithmic)
on imaginary array consisting of N + 1 elements each equal to its index in the array.
Space complexity is constant because array is 'imaginary' and binary search
is implemented in iterative manner (so that there is no need to allocate extra space to keep frames in the recursive function call stack).

## Search in a Rotated Sorted Array (rotated_binary_search.py)
* N - input array size
* Time Complexity: O(log(N))
* Space Complexity: O(1)

Essentially, this problem is solved by using binary search algorithm (hence, time complexity is logarithmic).
The only difference from 'classic' implementation of this algorithm (caused by rotation of sorted array)
is that extra care must be taken when deciding which half of the array next iteration of the algorithm will be concentrated on.
Space complexity is constant because binary search is implemented in iterative manner
(so that there is no need to allocate extra space to keep frames in the recursive function call stack).

## Rearrange Array Elements (rearrange_digits.py)
* N - input array size
* Time Complexity: O(N)
* Space Complexity: O(1)

To solve this problem, digit counts are calculated first. Note, that storing these counts do not contribute to the overall space complexity
because number of distinct digits is 10 which does not depend on size of the input array. Another reason for constant space complexity is that output numbers are calculated
on the fly by extracting 2 currently available maximum digits from 'counts' array and multiplying existing numbers by 10 and adding to them newly extracted digits.
Also, to avoid unnecessary traversal of digit counts from 9 to 0 every time, upper bound for not used yet digits is maintained.
Time complexity is linear because counts are calculated via single traversal of the input array and output numbers are calculated by extracting
each input digit from the 'counts' array exactly once.

## Dutch National Flag Problem (dutch_flag.py)
* N - input array size
* Time Complexity: O(N)
* Space Complexity: O(1)

This problem is solved using adoptation of the famous Dijkstra's
3-way partitioning scheme (which, btw, speeds up quicksort in case of many duplicate elements in the input array).
The idea is to choose 1 as pivot. After partition, all 1's will be in their places, so 0's and 2's will be in their too 'automatically'.
Time complexity is linear because during partition array traversed only once.
Because partition is done in place, space complexity is constant.

## Autocomplete with Tries (autocomplete.py)
* L - word length
* N - number of words stored in the trie
* Time Complexity: `Trie.insert`: O(L), `Trie.find`: O(L), `Trie.suffixes`: O(L * N)
* Space Complexity: `Trie.insert`: O(L * N), `Trie.find`: O(L * N), `Trie.suffixes`: O(L * N)

In the worst case, when prefixes are not shared between words, space of size O(L * N) will be required to store the trie.
Because `Trie.insert`, `Trie.find` and `Trie.suffixes` are member functions (methods) of the `Trie` class, they all have space complexity
of O(L * N) because in order for them to operate properly, corresponding trie instance must be hold in memory.
Also, when prefix suffixes requested for is empty, all words must be returned.
To collect all words from the trie, time of order O(L * N) is needed because the entire trie has to be traversed.
Note, because dictionary is used to store children nodes, alphabet size does not contribute to the formula for space complexity.
Also note that for maintaining currently built suffix, list is used to avoid unnecessary recreation of the entire strings via concatenation (because strings are immutable in python).
This fact speeds up the process and contributes to the overall time complexity (helps to make it linear in L).

## Max and Min in an Unsorted Array (min_max.py)
* N - input array size
* Time Complexity: O(N)
* Space Complexity: O(1)

To solve this problem, two variables corresponding to the currently found minimum and maximum elements are maintained.
Time complexity is linear because only single traversal of the input array is enough here.
Space complexity is constant because no extra space (of size dependent on the input size N) used during this traversal.
Note that in order to solve this problem there is no need to sort the array (btw, this problem is just a special case of search for k-th largest element in the array).

## Request Routing in a Web Server with a Trie (http_router.py)
* L - length of part of the URL
* P - number of parts in the URL
* N - number of URLs stored in the trie
* Time Complexity: `RouteTrie.insert`: O(L * P), `RouteTrie.find`: O(L * P), `Router.add_handler`: O(L * P), `Router.lookup`: O(L * P)
* Space Complexity: `RouteTrie.insert`: O(L * P * N), `RouteTrie.find`: O(L * P * N), `Router.add_handler`: O(L * P * N), `Router.lookup`: O(L * P * N)

In the worst case, when prefixes are not shared between URLs, space of size O(L * P * N) will be required to store the trie.
This fact leads to the O(L * P * N) space complexity for all methods of the `RouteTrie` class
(and of `Router` class methods as well because essentially they call corresponding methods from the `RouteTrie` class)
because in order for them to operate properly, corresponding trie instance must be hold in memory.
Note that L-factor is present because it is no longer the case that edges in the trie correspond to the single characters from the alphabet.
Instead, now they correspond to the parts (of length L) of the URLs.
Time complexity for both insert and lookup operations is O(L * P) because in both of them for each part of the route path
operations on strings of length L are performed (like their creation (during path splitting) and storing them in children dictionary).

