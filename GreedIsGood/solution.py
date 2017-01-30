import collections


def score(dice):
    dt = collections.Counter(dice)
    res = 0
    for index in xrange(2, 7):
        res += dt[index] / 3 * index * 100
    return res + dt[1] / 3 * 1000 + dt[1] % 3*100 + dt[5] % 3 * 50

print score([5, 1, 3, 4, 1])
print score([1, 1, 1, 3, 1])
print score([2, 4, 4, 5, 4])
	