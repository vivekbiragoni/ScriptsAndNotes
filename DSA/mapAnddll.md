## The advantages of **unordered_map** and **doubly linked list**, and then discuss how combining their strengths can lead to efficient data structures for various use cases.

### 1. **Advantages of `unordered_map`**:

- **Average O(1) Time Complexity**: The most significant advantage of `unordered_map` is that it provides **O(1)** average time complexity for insertions, deletions, and lookups. This is due to its underlying hash table structure, where elements are distributed across buckets based on hash values.
  
- **Efficient Key Lookup**: Unlike an ordered map, an `unordered_map` allows direct access to elements via their keys without requiring any order among the elements. This makes it ideal for scenarios where fast access and updates are needed, but the order of keys is irrelevant.

- **Flexibility of Key Types**: It supports a wide variety of key types, including strings, integers, and custom objects, as long as a valid hash function is provided.

### 2. **Advantages of Doubly Linked List**:

- **O(1) Insertion/Deletion at Both Ends**: A doubly linked list allows for **O(1)** insertion and deletion of elements from both the front and back (head and tail) of the list. Additionally, you can insert or delete elements at any position if you have a reference to the node, also in **O(1)** time.

- **Maintaining Order**: A doubly linked list maintains the relative order of elements, which can be useful when order matters (such as frequency of operations, or time of insertion).

- **Bidirectional Navigation**: Because each node has pointers to both its previous and next nodes, you can efficiently navigate in both directions (forward and backward). This feature is particularly useful when you need to traverse or rearrange elements in both directions.

### 3. **Combining `unordered_map` and Doubly Linked List**:

By combining the properties of `unordered_map` and a doubly linked list, you can build efficient data structures that offer both fast lookups and dynamic ordering of elements. This combination is useful for problems where you need to track elements in **O(1)** time, but also maintain their relative order for efficient access or updates.

#### Common Use Cases:

1. **LRU Cache (Least Recently Used Cache)**:
   - **Problem**: Design a cache that supports `get` and `put` operations in **O(1)** time, with the additional constraint that when the cache reaches its capacity, the least recently used item should be evicted.
   - **Solution**: 
     - Use an `unordered_map` to store key-value pairs for fast lookups.
     - Use a doubly linked list to store the order of access, where the least recently used element is at the head, and the most recently used element is at the tail.
     - When an element is accessed, move it to the tail of the list. If the cache exceeds capacity, remove the element from the head of the list (least recently used) and erase it from the map.

2. **All-One Data Structure (from your example)**:
   - **Problem**: Design a data structure that supports incrementing/decrementing keys, and retrieving the key with the maximum or minimum frequency in **O(1)** time.
   - **Solution**:
     - Use an `unordered_map` to store each key and its frequency.
     - Use a doubly linked list to maintain the frequency buckets in increasing order. Each node in the list holds a set of keys with the same frequency.
     - When a key’s frequency changes, update the list to reflect the change, and move the key to the appropriate bucket.

3. **Frequent Elements Tracker**:
   - **Problem**: You need to track elements and their frequencies, such that you can quickly retrieve the most/least frequent element.
   - **Solution**:
     - Use an `unordered_map` to store the frequency of each element.
     - Use a doubly linked list to maintain the frequency of elements in increasing order, where each node represents a specific frequency and stores the elements with that frequency.
     - When an element's frequency changes, you can move it to the appropriate position in the list.

#### Example: Optimizing with `unordered_map` + Doubly Linked List

Let's revisit the idea of combining `unordered_map` and doubly linked list for efficient retrieval of min/max keys, similar to the **All-One** data structure:

- **Unordered_map for Direct Access**:
  - Store the keys and their corresponding frequency in an `unordered_map`. This allows **O(1)** access to update the frequency of any key.
  - Additionally, store a second `unordered_map` to map each frequency to a node in the doubly linked list, where the node contains all the keys that share that frequency.

- **Doubly Linked List for Ordered Frequency Buckets**:
  - The doubly linked list will maintain the order of frequencies. Each node represents a frequency (e.g., count = 1, count = 2, etc.) and contains a set of keys that have that frequency.
  - When a key's frequency increases or decreases, you can move it between frequency nodes efficiently, adjusting the list order only when necessary.

This combination ensures that:
- **O(1) Access to Keys** via the `unordered_map`.
- **O(1) Frequency Adjustment** by moving keys between frequency nodes in the linked list.
- **O(1) Retrieval of Max/Min Frequency Keys** since the linked list's head and tail always hold the least and most frequent elements, respectively.

### Final Thoughts:

- **Best of Both Worlds**: Combining `unordered_map` and doubly linked list gives you both fast lookups and efficient, ordered data management. The `unordered_map` provides O(1) access to elements, while the doubly linked list allows for efficient ordered operations like finding the most or least frequent element.
  
- **Trade-Off**: You might need to manage more memory and pointers (as in a linked list), but you gain huge improvements in time complexity for operations that would otherwise take **O(n)** time in a naive approach.

By leveraging this combination, you can solve a variety of problems in **constant time** while maintaining some ordering, which is crucial for many optimization problems like caching, frequency counting, or even queue-like structures where order and fast access are both necessary.

Let's walk through an example of the **All-One** data structure with a visual representation using text. This structure efficiently tracks keys and their frequencies, and allows for fast retrieval of keys with the maximum and minimum frequencies.

### Example Walkthrough:

1. **Start with an empty All-One structure.**
2. **Operations to perform**:
   - `inc("a")`
   - `inc("b")`
   - `inc("a")`
   - `inc("c")`
   - `inc("b")`
   - `dec("a")`
   - `inc("d")`
   - `getMaxKey()` and `getMinKey()`

### Step-by-Step:

#### 1. Initial State (empty):
- No keys have been inserted yet, so both the hash maps (`keyCount` and `countBucket`) and the doubly linked list are empty.

```text
(keyCount): { }
(countBucket): { }
(Linked List): (Empty)
```

#### 2. Operation: `inc("a")`

- `"a"` is inserted with frequency 1.
- Since there is no frequency bucket for 1 yet, create a new node for frequency 1 in the doubly linked list.

```text
(keyCount): { "a": 1 }
(countBucket): { 1 -> [a] }
(Linked List):
  [1] -> { a }
```

#### 3. Operation: `inc("b")`

- `"b"` is inserted with frequency 1.
- Since there is already a frequency 1 bucket, add `"b"` to that bucket.

```text
(keyCount): { "a": 1, "b": 1 }
(countBucket): { 1 -> [a, b] }
(Linked List):
  [1] -> { a, b }
```

#### 4. Operation: `inc("a")`

- `"a"` is incremented, so its frequency becomes 2.
- `"a"` is removed from the frequency 1 bucket.
- A new frequency 2 bucket is created, and `"a"` is added to that bucket.

```text
(keyCount): { "a": 2, "b": 1 }
(countBucket): { 1 -> [b], 2 -> [a] }
(Linked List):
  [1] -> { b } -> [2] -> { a }
```

#### 5. Operation: `inc("c")`

- `"c"` is inserted with frequency 1.
- `"c"` is added to the existing frequency 1 bucket.

```text
(keyCount): { "a": 2, "b": 1, "c": 1 }
(countBucket): { 1 -> [b, c], 2 -> [a] }
(Linked List):
  [1] -> { b, c } -> [2] -> { a }
```

#### 6. Operation: `inc("b")`

- `"b"` is incremented, so its frequency becomes 2.
- `"b"` is removed from the frequency 1 bucket and added to the frequency 2 bucket.

```text
(keyCount): { "a": 2, "b": 2, "c": 1 }
(countBucket): { 1 -> [c], 2 -> [a, b] }
(Linked List):
  [1] -> { c } -> [2] -> { a, b }
```

#### 7. Operation: `dec("a")`

- `"a"` is decremented, so its frequency becomes 1.
- `"a"` is moved from the frequency 2 bucket to the frequency 1 bucket.

```text
(keyCount): { "a": 1, "b": 2, "c": 1 }
(countBucket): { 1 -> [a, c], 2 -> [b] }
(Linked List):
  [1] -> { a, c } -> [2] -> { b }
```

#### 8. Operation: `inc("d")`

- `"d"` is inserted with frequency 1.
- `"d"` is added to the existing frequency 1 bucket.

```text
(keyCount): { "a": 1, "b": 2, "c": 1, "d": 1 }
(countBucket): { 1 -> [a, c, d], 2 -> [b] }
(Linked List):
  [1] -> { a, c, d } -> [2] -> { b }
```

#### 9. Operation: `getMaxKey()`

- The max key is the key in the highest frequency bucket (which is at the tail of the doubly linked list). The max frequency is 2, so one of the keys from that bucket is `"b"`.
  
```text
Max Key: "b"
```

#### 10. Operation: `getMinKey()`

- The min key is the key in the lowest frequency bucket (which is at the head of the doubly linked list). The min frequency is 1, so one of the keys from that bucket is `"a"`, `"c"`, or `"d"`. Let's assume we return `"a"`.
  
```text
Min Key: "a"
```

### Final Structure:

```text
(keyCount): { "a": 1, "b": 2, "c": 1, "d": 1 }
(countBucket): { 1 -> [a, c, d], 2 -> [b] }
(Linked List):
  [1] -> { a, c, d } -> [2] -> { b }
```

### Breakdown:

- **keyCount**: Maps each key to its frequency (e.g., `"a"` has frequency 1, `"b"` has frequency 2).
- **countBucket**: Maps each frequency to a set of keys that share the same frequency.
- **Doubly Linked List**: Keeps the frequency buckets in order. The head of the list has the minimum frequency (1 in this case), and the tail has the maximum frequency (2 in this case).

- **Max Key** is obtained from the tail of the list.
- **Min Key** is obtained from the head of the list.

### Efficiency:

By using both an `unordered_map` for fast lookups and a **doubly linked list** to maintain frequency order, this structure allows efficient **O(1)** operations for `inc()`, `dec()`, `getMaxKey()`, and `getMinKey()`, even as the number of elements grows.
