## LRU Cache (lru_cache.py)
* N - number of items currently present in cache
* Time Complexity: `set`: O(1), `get`: O(1)
* Space Complexity: O(N)

In order to achieve constant time complexity of `set` and `get` operations,
`LRU_Cache` is implemented by employing both doubly linked list and dictionary data structures.
Doubly linked list maintains order of items usage: newly added items are appended (in constant time) to the end of the list
and items already present in cache are moved (*cut* and *pasted*, also in constant time) to the end of the list on lookup or update.
This way, when cache reaches its full capacity, least recently used item will always be at the beginning of the list and will be removed in constant time.
Dictionary is used 'on top of' (dict *values* refer to the list *nodes*) doubly linked list to ensure constant time lookup.
Space occupied by instance of `LRU_Cache` class is proportional to the number of nodes and, hence, to the number of elements currently present in cache.

## File Recursion (file_recursion.py)
* N - total number of entries (both file and directory) beneath given path
* Time Complexity: O(N)
* Space Complexity: O(N)

`find_files` function is implemented using recursive variant of depth first search algorithm.
In order to find all files with the given suffix, all entries inside the corresponding file system subtree
must be visited, hence linear time complexity. In case of degenerate file system subtree (i.e., when it resembles a linked list),
maximum depth of recursion will be very close or equal to the number of entries in a subtree.
Because space required by such recursive algorithm is proportional to the maximum depth of recursion (in order to keep frames in call stack),
(worst case) space complexity is linear as well.

## Huffman Coding (huffman.py)
* N - number of characters in input string (proportional to the number of bits occupied by them)
* M - numbers of bits in Huffman code
* Time Complexity: `huffman_encoding`: O(N * log(N)), `huffman_decoding`: O(M)
* Space Complexity: `huffman_encoding`: O(N), `huffman_decoding`: O(M)

To implement `huffman_encoding` function, dictionary mapping symbols from the input string to their frequencies of appearance is created first.
Then, instance of `HuffmanTree` class is built using this dictionary and employing min-heap based priority queue data structure.
This data structure makes it possible to build such a tree in linearithmic time O(N * log(N)).
Because Huffman tree is a binary tree with number of leaves not greater than the number of characters in the input string, space occupied by this tree would be linear in the worst case (i.e., O(N)).
`huffman_decoding` function essentially iterates over bits from the input Huffman code doing constant time operations per bit. Hence, its time complexity is linear in the input size (i.e., O(M)).
To achieve this constant time per bit complexity, intermediate *accumulator* list is built (from which output string is finally constructed).
This *accumulator* list is needed to avoid multiple string concatenations leading to the worst case quadratic time complexity (strings are immutable in Python).
Because in the worst case number of characters in the decoded string will be equal to the number of bits in the input code string, space complexity of `huffman_decoding` function is linear (i.e., O(M)).

## Active Directory (active_dir.py)
* N - total number of groups in the given group hierarchy
* Time Complexity: O(N)
* Space Complexity: O(N)

`is_user_in_group` function is implemented using recursive variant of depth first search algorithm.
It is worth noting that search stops as soon as user is found inside some group reachable from the root.
To conclude that user does not belong to the group, all nodes from the corresponding graph must be visited at least once.
To ensure that every node is explored **at most** once and, hence, significantly speed up search (specifically, make it linear time), `visited` set is employed. 
Space complexity is also linear because in the worst case all groups will be added to that `visited` set.
Worst case space complexity won't change even in case cache of visited nodes is absent.
This is because maximum recursion depth (which is proportional to space needed to keep active frames in the call stack)
could be equal to the total number of groups in the hierarchy (in cases of degenerate graphs resembling linked lists).

## Blockchain (blockchain.py)
* N - number of blocks in blockchain
* Time Complexity: `add_block`: O(1), `is_valid`: O(N)
* Space Complexity: O(N)

Blockchain is implemented internally as a linked list in which both *head* and *tail* are maintained.
Because *tail* could be accessed in constant time, `add_block` method has constant time complexity.
Blockchain validation has linear time complexity because hashes need to be verified for every block.
Space occupied by instance of Blockchain class is proportional to the number of blocks added to the chain,
hence space complexity is linear in number of blocks.

## Union and Intersection (union_intersection.py)
* N1 - number of elements in first list
* N2 - number of elements in second list
* Time Complexity: `union`: O(N1 + N2), `intersection` O(N1 + N2)
* Space Complexity: `union` O(N1 + N2), `intersection` O(min(N1, N2))

In order to implement `union` function, elements from both linked lists are added to the same set.
This set is exactly the *union* of two lists. Then, because function need to return a linked list, set is converted to the list.
Creating such set and converting it back to the linked list (in worst case) takes linear time and space in number of elements from both input lists added together.
Intersection of two lists won't contain more elements than size of a smaller list. This observation is exploited in the implementation of the `intersection` function.
Specifically, to make necessary lookups constant time, `set_2` is created from the list of smaller size.
Then, by iterating over the list of bigger size, elements are added to the `intersection_set` only if they are present in `set_2`.
So, size of `intersection_set` won't be bigger than size of `set_2`. Hence, space complexity of the entire algorithm is O(min(N1, N2)).
Time complexity is O(N1 + N2) because set from smaller list has to be created and iteration over bigger list has to be performed.
Finally, resulting linked list is created from the `intersection_set`. Note, that this intermediate `intersection_set` is needed
to prevent duplicate values from appearing in the resulting linked list.

