# Top 50 Programming questions asked in an interview (from [SimpleProgrammer](https://content.techgig.com/hiring/20-most-frequently-asked-programming-interview-questions/articleshow/74608663.cms))

## Array Coding Interview Questions:
[1. How do you find the missing number in a given integer array of 1 to 100?](#1-how-do-you-find-the-missing-number-in-a-given-integer-array-of-1-to-100)
[2. How do you find the duplicate number on a given integer array?](#2-how-do-you-find-the-duplicate-number-on-a-given-integer-array)
[3. How do you find the largest and smallest number in an unsorted integer array?](#3-how-do-you-find-the-largest-and-smallest-number-in-an-unsorted-integer-array)
[4. How do you find all pairs of an integer array whose sum is equal to a given number?](#4-how-do-you-find-all-pairs-of-an-integer-array-whose-sum-is-equal-to-a-given-number)
[5. How do you find duplicate numbers in an array if it contains multiple duplicates?](#5-how-do-you-find-duplicate-numbers-in-an-array-if-it-contains-multiple-duplicates)
[6. How are duplicates removed from a given array in Java?]
[7. How is an integer array sorted in place using the quicksort algorithm?]
[8. How do you remove duplicates from an array in place?]
[9. How do you reverse an array in place in Java?]
[10. How are duplicates removed from an array without using any library?]

## Answers
> ### 1. How do you find the missing number in a given integer array of 1 to 100?
<p>Add up 2 sums: one from the integer array, and another is from 1 to 100. Subtract both from each other to get the missing number</p>

```
def missingNum(nums):
    # nums = list of integers
    sum_of_ints = sum(nums)
    len_of_100 = sum(range(1,101))
    return len_of_100 - sum_of_ints
```

> ### 2. How do you find the duplicate number on a given integer array?
<p>1. Create a hash_set of counter of all integers in the array. Return the one where counter > 1</p>
<p>2. Sort the array. If nums[i] == nums[i-1], then return nums[i]</p>

[Leetcode 287. Find the Duplicate Number](https://leetcode.com/problems/find-the-duplicate-number/)

```
# Using set()
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        output = set()
        for n in nums:
            if n in output:
                return n
            else:
                output.add(n)

# Use collections.Counter                
from collections import Counter
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums_count = Counter(nums)
        for key, val in nums_count.items():
            if val > 1:
                return key

# Sorting Solution
class Solution:                
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                return nums[i]
```

> ### 3. How do you find the largest and smallest number in an unsorted integer array?
<p>Initiate 2 variables (min and max val). Iterate thru the array, each time comparing larger and smaller ones</p>

```
def largestSmallest(nums):
    smaller = nums[0]
    larger = nums[0]

    for i in range(1, len(nums)):
        if nums[i] < smaller:
            smaller = nums[i]
        if nums[i] > larger:
            larger = nums[i]
    
    return (smaller, larger)
```

> ### 4. How do you find all pairs of an integer array whose sum is equal to a given number?
<p>Iterate thru all array items O(n2) -> each time, checking if the sum is == target sum</p>

```
def countPairs(nums):
    output = list()
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            two_sum = nums[i] + nums[j]
            if two_sum == target:
                output.append(nums[i],nums[j])
    return output
```

<p>ref: to this Leetcode Qn: Two Sum (similar - but this qn only has 1 pair each target)</p>

[Related: Leetcode 1. Two Sum](https://leetcode.com/problems/two-sum/)

```
# Leetcode Ans
def twoSum(self, nums: List[int], target: int) -> List[int]:
    nums_dict = dict()
    
    for i in range(len(nums)):
        diff = target - nums[i]
        
        if diff in nums_dict.keys():
            return (i, nums_dict[diff])
        else:
            nums_dict[nums[i]] = i
```

> ### 5. How do you find duplicate numbers in an array if it contains multiple duplicates?
<p>Use a hash_map to count the frequency of the numbers in the array. Return those where frequency >= 2</p>

[Leetcode 442. Find All Duplicates in an Array](https://leetcode.com/problems/find-all-duplicates-in-an-array/)

```
# Use Python collections.Counter
from collections import Counter
def findDuplicates(self, nums: List[int]) -> List[int]:
    nums_count = Counter(nums)
    output = list()
    
    for key, val in nums_count.items():
        if val >= 2:
            output.append(key)
    
    return output

# Use Sorting
def findDuplicates(self, nums: List[int]) -> List[int]:
    nums.sort()
    print(nums)
    left = 0
    output = list()
    
    for i in range(1, len(nums)):
        if nums[i] != nums[left]:
            left += 1
        else:
            output.append(nums[left])
            left += 1
            
    return output
```


---

## Linked List Programming Interview Questions:
[11. How do you find the middle element of a singly linked list in one pass?]
[12. How do you check if a given linked list contains a cycle? How do you find the starting node of the cycle?]
[13. How do you reverse a linked list?]
[14. How do you reverse a singly linked list without recursion?]
[15. How are duplicate nodes removed in an unsorted linked list?]
[16. How do you find the length of a singly linked list?]
[17. How do you find the third node from the end in a singly linked list?]
[18. How do you find the sum of two linked lists using Stack?]

## String Coding Interview Questions:
[19. How do you print duplicate characters from a string?]
[20. How do you check if two strings are anagrams of each other?]
[21. How do you print the first non-repeated character from a string?]
[22. How can a given string be reversed using recursion?]
[23. How do you check if a string contains only digits?]
[24. How are duplicate characters found in a string?]
[25. How do you count a number of vowels and consonants in a given string?]
[26. How do you count the occurrence of a given character in a string?]
[27. How do you find all permutations of a string?]
[28. How do you reverse words in a given sentence without using any library method?]
[29. How do you check if two strings are a rotation of each other?]
[30. How do you check if a given string is a palindrome?]

## Binary Tree Coding Interview Questions:
[31. How is a binary search tree implemented?]
[32. How do you perform preorder traversal in a given binary tree?]
[33. How do you traverse a given binary tree in preorder without recursion?]
[34. How do you perform an inorder traversal in a given binary tree?]
[35. How do you print all nodes of a given binary tree using inorder traversal without recursion?]
[36. How do you implement a postorder traversal algorithm?]
[37. How do you traverse a binary tree in postorder traversal without recursion?]
[38. How are all leaves of a binary search tree printed?]
[39. How do you count a number of leaf nodes in a given binary tree?]
[40. How do you perform a binary search in a given array?]

## Miscellaneous Coding Interview Questions:
[41. How is a bubble sort algorithm implemented?]
[42. How is an iterative quicksort algorithm implemented?]
[43. How do you implement an insertion sort algorithm?]
[44. How is a merge sort algorithm implemented?]
[45. How do you implement a bucket sort algorithm?]
[46. How do you implement a counting sort algorithm?]
[47. How is a radix sort algorithm implemented?]
[48. How do you swap two numbers without using the third variable?]
[49. How do you check if two rectangles overlap with each other?]
[50. How do you design a vending machine?]