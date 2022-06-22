def flatten(nums):
    # recursive base case
    if nums == []:
        return nums

    # remove one layer of list
    if type(nums[0]) == list:
        return flatten(nums[0]) + flatten(nums[1:])

    # accumulate output
    return [nums[0]] + flatten(nums[1:])

def radix(nums):
    # create width
    width = len(str(max(nums)))

    for power in range(width):
        # create buckets
        bucket = [[] for _ in range(10)]

        # assign nums into buckets
        for n in nums:
            bucket_idx = n // (10**power) % 10
            bucket[bucket_idx].append(n)

        # flatten bucket back into nums (for next iteration)
        nums = flatten(bucket)
    return nums

var = [221,103,111,428,329,853]
print(radix(var))

var = [2, 0, 1]
print(radix(var))