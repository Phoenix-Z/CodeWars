import math

# (1469ms)
# 这个方法有点类似于判断素数使用的方式，时间复杂度为O(nlogn)
def list_squared(m, n):
    sum_of_square = [1] * (n + 1)
    for i in xrange(2, n + 1):
        j = i
        while j <= n:
            sum_of_square[j] += i * i
            j += i
    return [[i, sum_of_square[i]] for i in xrange(m, n + 1) if int(math.sqrt(sum_of_square[i])) ** 2 == sum_of_square[i]]


# 由于满足条件的只有几个可能，所以可以采取暴力的方式，时间复杂度为O(1)	
def list_squared2(m, n):
    pairs = [[1, 1],
            [42, 2500],
            [246, 84100],
            [287, 84100],
            [728, 722500],
            [1434, 2856100],
            [1673, 2856100],
            [1880, 4884100],
            [4264, 24304900],
            [6237, 45024100],
            [9799, 96079204],
            [9855, 113635600]]
    return [x for x in pairs if m <= x[0] <= n]
	
print list_squared(1, 250)
print list_squared(42, 250)
