# coding:utf-8


# (10410ms)
# 这是用空间换取时间的做法，虽然由于需要创造大数组导致所花费的时间很多，而且数组的大小
# 随着传入的参数大小而剧增，所以这个方法虽然通过了样例，但依然不值得提倡。
def dbl_linear(n):

    u = [False] * 10000000
    u[1] = True
    for index, x in enumerate(u):
        if x:
            u[2 * index + 1] = True
            u[3 * index + 1] = True
            if n == 0:
                return index
            n -= 1


# (941ms)
# 这是一个比较合适的做法，即不是讲两种类型的数字放在同一个list中，而是分开存放，
# 需要添加新的元素中，只需要查看两个队列头中较小的数字即可，直到遇到第n个数字。
def dbl_linear2(n):
    double, trible = [1], [1]
    i, j = 0, 0
    while n >= 0:
        num = min(double[i], trible[j])
        double.append(2 * num + 1)
        trible.append(3 * num + 1)
        if n == 0:
            return num
        if num == double[i]:
            i += 1
        if num == trible[j]:
            j += 1
        n -= 1


print dbl_linear2(0)
print dbl_linear2(1)
print dbl_linear2(10)
print dbl_linear2(20)
print dbl_linear2(100)