# Good morning! Here's your coding interview problem for today.

# This problem was asked by Stripe.

# Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

# For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

# You can modify the input array in-place.

#in place
#runtime O(n+nlogn)
#easy solution
def LowestMissingSorted(arr):
    arr.sort()
    prev = 0
    for ele in arr:
        if ele <= 0 or ele == prev:
            continue
        if ele != prev + 1:
            return prev + 1
        prev = ele
    return prev + 1

#no sorting
#runtime O(2n)
#not in place though
#n 
def LowestMissing(arr):
    newArr = [0] * len(arr)
    for i in range(len(arr)):
        if(arr[i] < 1 or arr[i] > len(arr)):
            continue
        newArr[arr[i]-1] = -1
    for i in range(len(newArr)):
        if(newArr[i] == 0):
            return i + 1
    return len(arr) + 1

arr = [3,4,7,1,2,5,-6,-7]
print(LowestMissing(arr))