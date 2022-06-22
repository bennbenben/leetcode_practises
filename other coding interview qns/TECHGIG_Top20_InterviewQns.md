# Top 20 Programming questions asked in an interview (from [TECHGIG](https://content.techgig.com/hiring/20-most-frequently-asked-programming-interview-questions/articleshow/74608663.cms))

## Questions:
[1. How is a bubble sort algorithm implemented?](#1.-how-is-a-bubble-sort-algorithm-implemented?)<br/>
[2. How to print the first non-repeated character from a string?](#2-how-to-print-the-first-non-repeated-character-from-a-string)<br/>
[3. How to find the first non repeated character of a given String?](#3-how-to-find-the-first-non-repeated-character-of-a-given-string)<br/>
[4. How do you find duplicate numbers in an array if it contains multiple duplicates?](#4-how-do-you-find-duplicate-numbers-in-an-array-if-it-contains-multiple-duplicates)<br/>
[5. How do you remove duplicates from an array in place?](#5-how-do-you-remove-duplicates-from-an-array-in-place)<br/>
[6. How are duplicates removed from an array without using any library?](#6-how-are-duplicates-removed-from-an-array-without-using-any-library)<br/>
[7. How do you find the middle element of a singly linked list in one pass?](#7-how-do-you-find-the-middle-element-of-a-singly-linked-list-in-one-pass)<br/>
[8. How do you check if a given linked list contains a cycle? How will you find initial node of the cycle?](#8-how-do-you-check-if-a-given-linked-list-contains-a-cycle-how-will-you-find-initial-node-of-the-cycle)<br/>
[9. How do you reverse a singly linked list without recursion?](#9-how-do-you-reverse-a-singly-linked-list-without-recursion)<br/>
[10. How is a binary search tree implemented?](#10-how-is-a-binary-search-tree-implemented)<br/>
[11. How do you traverse a given binary tree in preorder without recursion?](#11-how-do-you-traverse-a-given-binary-tree-in-preorder-without-recursion)<br/>
[12. How do you print all nodes of a given binary tree using inorder traversal without recursion?](#12-how-do-you-print-all-nodes-of-a-given-binary-tree-using-inorder-traversal-without-recursion)<br/>
[13. How is a merge sort algorithm implemented?](#13-how-is-a-merge-sort-algorithm-implemented)<br/>
[14. How is a radix sort algorithm implemented?](#14-how-is-a-radix-sort-algorithm-implemented)<br/>
[15. How do you swap two numbers without using the third variable?](#15-how-do-you-swap-two-numbers-without-using-the-third-variable)<br/>
[16. How do you design a vending machine?](#16-how-do-you-design-a-vending-machine)<br/>
[17. Write a program to find prime factors of an integer?](#17-write-a-program-to-find-prime-factors-of-an-integer)<br/>
[18. What is Depth First Search Algorithm for a binary tree?](#18-what-is-depth-first-search-algorithm-for-a-binary-tree)<br/>
[19. Difference between a stable and unstable sorting algorithm?](#19-difference-between-a-stable-and-unstable-sorting-algorithm)<br/>
[20. What is the difference between Comparison and Non-Comparison Sorting Algorithms?](#20-what-is-the-difference-between-comparison-and-non-comparison-sorting-algorithms)

---

## Answers

> ### 1. How is a bubble sort algorithm implemented?
<p>Bubble sort is implemented by comparing adjacent elements until the entire array is sorted. It needs one full pass to know that it's fully sorted</p>

```
def bubblesort(nums):
    for i in range(len(nums)):
        swapped = False
        for j in range(0, len(nums)-1-i):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
                swapped = True
        # one pass has confirmed that elements are already in sorted place
        if swapped == False:
            break
```
> ### 2. How to print the first non-repeated character from a string?
<p>Create a hash map of the letters and its respective counts</p>
<p>Iterate through the hashmap and return where the count == 1</p>

[Leetcode Qn 387. First Unique Character in a String](https://leetcode.com/problems/first-unique-character-in-a-string/)

```
class Solution:
    def firstUniqChar(self, s: str) -> int:
        s_counts = {}
        
        for letter in s:
            if letter not in s_counts.keys():
                s_counts[letter] = 1
            else:
                s_counts[letter] += 1
        
        for key, val in s_counts.items():
            if val == 1:
                return s.index(key)
        return -1
```

> ### 3. How to find the first non repeated character of a given String?
<p>Same as above #2</p>

> ### 4. How do you find duplicate numbers in an array if it contains multiple duplicates?
<p>Create a counter's hash map and populate it: {number: count}</p>
<p>Then iterate through it. It count == 2, append the number to another list</p>
<p>Finally, return the list</p>

[Leetcode Qn 442. Find All Duplicates in an Array](https://leetcode.com/problems/find-all-duplicates-in-an-array/)

```
def findDuplicates(self, nums: List[int]) -> List[int]:
        nums_count = Counter(nums)
        output = list()
        for key, val in nums_count.items():
            if val == 2:
                output.append(key)
        return output
```

> ### 5. How do you remove duplicates from an array in place?
<p>Iterate through the array from idx 1 onwards while holding a left pointer</p>
<p>If nums[i] == nums[i-1]: assign the left pointer to nums[i] and increment left ptr by 1</p>

[Leetcode Qn 26. Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/)

```
def removeDuplicates(self, nums: List[int]) -> int:
    left = 1
    
    for i in range(1, len(nums)):
        if nums[i] == nums[i-1]:
            continue
        else:
            nums[left] = nums[i]
            left += 1

    return left
```

> ### 6. How are duplicates removed from an array without using any library?
<p>Create a counter dictionary of the array (after iterating and counting thru it)</p>
<p>Afterwards, iterate thru the dictionary. Run the list.remove method for x number of times</p>

> ### 7. How do you find the middle element of a singly linked list in one pass?
<p>Iterate from the first Node with slow and fast pointer. Slow += 1, fast += 2</p>
<p>while loop condition - if fast and fast.next:</p>

[Leetcode Qn 876. Middle of the Linked List](https://leetcode.com/problems/middle-of-the-linked-list/)

```
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast, slow = head, head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
```

> ### 8. How do you check if a given linked list contains a cycle? How will you find initial node of the cycle?
<p>Use a hash set to store all the nodes (while iterating thru them). If encounter a Node that is in the hash set, then cycle exists</p>

[Leetcode 141. Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/)

```
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        
        visited = set()
        curr_node = head
        
        while curr_node:
            if curr_node not in visited:
                visited.add(curr_node)
            else:
                return True
            
            curr_node = curr_node.next
        
        return False
```

> ### 9. How do you reverse a singly linked list without recursion?
<p>Initialize a None node, then iterate through the LL</p>
<p>Each time, reversing the node's pointer</p>

[Leetcode 206. Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/)

```
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev_node = None
        curr_node = head
        
        while curr_node:
            # Save pointers
            next_node = curr_node.next
            # Reverse pointers
            curr_node.next = prev_node
            # Update pointers
            prev_node = curr_node
            curr_node = next_node
        
        return prev_node
```

> ### 10. How is a binary search tree implemented?
<p>A binary tree where each node has an associated value. It allows fast lookup, addition, and removal of items</p>
<p>Require 2 classes - Node & BST</p>

[Answer from here](https://www.educative.io/answers/how-do-you-implement-a-binary-search-tree-in-multiple-languages)

```
# Node Class
class Node:
    # Default Constructor
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    # A utility function to insert a new node with given val in BST
    def insert(self, val):
      
      # If the tree is empty, return a new node
      if not self:
        self = Node(val)
        return
      
      # Otherwise, recur down the tree
      if val < self.val:
        if self.left:
          self.left.insert(val)
        else:
          self.left = Node(val)
          return      
      else:
        if self.right:
          self.right.insert(val)
        else:
          self.right = Node(val)
          return
        
# BST Class    
class binarySearchTree:
    def __init__(self, val):
        self.root = Node(val)
    
    def insert(self, val):
      self.root.insert(val)
      
# A utility function to do inorder tree traversal 
def inorder(root): 
  if root: 
    inorder(root.left) 
    print(root.val) 
    inorder(root.right) 
  
# Let's create the above Binary Search Tree

BST = binarySearchTree(6)

BST.insert(3)
BST.insert(9)
BST.insert(1)
BST.insert(5)
BST.insert(7)
BST.insert(11)

# Print inoder traversal of the BST 
inorder(BST.root)
```

> ### 11. How do you traverse a given binary tree in preorder without recursion?
<p>Use the iterative way</p>

[Leetcode 144. Binary Tree Preorder Traversal](https://leetcode.com/problems/binary-tree-preorder-traversal/)

```
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return
        
        stack, output = list(), list()
        stack.append(root)
        
        while stack:
            curr_node = stack.pop()
            
            if curr_node:
                output.append(curr_node.val)
            
            if curr_node.right:
                stack.append(curr_node.right)
                
            if curr_node.left:
                stack.append(curr_node.left)
        
        return output
```

> ### 12. How do you print all nodes of a given binary tree using inorder traversal without recursion?
<p>Inorder - Left, Root, Right</p>

[Leetcode 94. Binary Tree Inorder Traversal](https://leetcode.com/problems/binary-tree-inorder-traversal/)

```
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        output = []
        
        curr_node = root
        
        while curr_node or stack:
            while curr_node:
                stack.append(curr_node)
                curr_node = curr_node.left
            
            curr_node = stack.pop()
            output.append(curr_node.val)
            curr_node = curr_node.right

        print(output)
        return output
```

> ### 13. How is a merge sort algorithm implemented?
<p>Merge Sort is a stable and recursive sorting algorithm. It splits elements into individual ones before joining them back together (sorted)</p>
<p>Time complexity: O(nLogn)</p>
<p>Space complexity: O(n)</p>

[Leetcode 75. Sort Colors](https://leetcode.com/problems/sort-colors/)

```
def merge_sort(nums):
    if len(nums)>1:
        # Recursively split array into halves
        mid = len(nums)//2
        left = nums[:mid]
        right = nums[mid:]
        
        merge_sort(left)
        merge_sort(right)
        
        # merge portion
        i,j,k = 0,0,0
        
        while i<len(left) and j<len(right):
            if left[i] < right[j]:
                nums[k] = left[i]
                i += 1
                k += 1
            else:
                nums[k] = right[j]
                j += 1
                k += 1
        
        # transfer remaining elements in left into nums
        while i<len(left):
            nums[k] = left[i]
            k += 1
            i += 1
        
        # transfer remaining elements in right into nums
        while j<len(right):
            nums[k] = right[j]
            k += 1
            j += 1
```

> ### 14. How is a radix sort algorithm implemented?
<p>Radix sort is a stable sorting algorithm that uses counting sort as a subroutine</p>
<p>It sorts by significant digit's places into buckets, from the least sig fig to the most sig fig</p>
<p>Time complexity is O(N*K), where N is number of elements in the array, and K is the len(largest digit in array)</p>
<p>Space complexity is O(N+K), because it creates multiple arrays in between</p>

```
def flatten(num):
    if num == []:
        return num

    if type(num[0]) == list:
        return flatten(num[0]) + flatten(num[1:])

    return num[:1] + flatten(num[1:])
        

def radix(nums):
    # length of largest digit
    nums_digits = len(str(max(nums)))
    
    # iterate thru nums for n times, where n = nums_digits
    # each time, doing a bucket sort
    for digit in range(0, nums_digits):
        bucket, flatten_bucket = list(), list()
        for _ in range(10):
            bucket.append([])
        
        # start classifying items by buckets
        for item in nums:
            bucket_num = item // (10**digit) % 10
            bucket[bucket_num].append(item)
        flatten_bucket = flatten(bucket)
    return flatten_bucket

var = [2,0,2,1,1,0]
print(radix(var))

var = [2,0,1]
print(radix(var))
```

> ### 15. How do you swap two numbers without using the third variable?
1. Use python in-built
```
x, y = 10, 20
print ("Before swapping: ")
print("Value of x : ", x, " and y : ", y)
x, y = y, x
print ("After swapping: ")
print("Value of x : ", x, " and y : ", y)
```
2. Use Add/Sub Operators
```
x, y = 10, 20
print ("Before swapping: ")
print("Value of x : ", x, " and y : ", y)
x = x + y
y = x - y
x = x - y
print ("After swapping: ")
print("Value of x : ", x, " and y : ", y)
```
3. Use Multiply/Divide Operators
```
x, y = 10, 20
print ("Before swapping: ")
print("Value of x : ", x, " and y : ", y)
x = x * y
y = x / y
x = x / y
print ("After swapping: ")
print("Value of x : ", x, " and y : ", y)
```

> ### 16. How do you design a vending machine?

> ### 17. Write a program to find prime factors of an integer?
<p>Initialize a variable prime = 2. Use a while loop to track if (nums > 1). Each time, if nums is divisible by prime, then execute it and track prime</p>
<p>Else, increment prime by 1</p>

```
def primeFactors(nums):
    prime = 2
    output = list()
    while nums > 1:
        if nums % prime == 0:
            nums = nums / prime
            output.append(prime)
        else:
            prime += 1
    return output
```

> ### 18. What is Depth First Search Algorithm for a binary tree?
<p>It is a backtracking (recursive) way for traversing a binary tree. The deepest node is reached first, then backtracks to its parent node (if it has no child nodes)</p>

> ### 19. Difference between a stable and unstable sorting algorithm?
<p>Mainly on how the algorithm treats equal (or repeated) elements</p>
<p>Stable sorting algorithms preserve the relative order of equal elements, while unstable sorting algorithms don’t</p>

![Snippet showing stable vs unstable sorting algos](https://www.baeldung.com/wp-content/uploads/2019/08/Stable-vs-Unstable-1.png)

> ### 20. What is the difference between Comparison and Non-Comparison Sorting Algorithms?
<p>Comparison sorting algorithmns have a comparison operator - like smaller than or bigger than</p>
<p>Sorting algorithms that sort the data without comparing the elements are called non-comparison sorting</p>