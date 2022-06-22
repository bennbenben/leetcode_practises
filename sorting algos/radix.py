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