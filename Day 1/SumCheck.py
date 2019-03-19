# This problem was recently asked by Google.

# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

# Bonus: Can you do this in one pass?

items = [10, 15, 3, 7]
k = 17

def SumCheck(items, k):
    items.sort()
    cursor1 = 0
    cursor2 = len(items) - 1
    while cursor1 != cursor2:
        curSum = items[cursor1] + items[cursor2]
        if curSum == k:
            return True
        elif curSum < k:
            cursor1 += 1
        else:
            cursor2 -= 1
        pass
    return False

print(SumCheck(items, k))

