def hamming(n):
    """Returns the nth hamming number"""
    # 找出hamming number 与twice linear那道题目的思想是基本一致的，只不过需要多加一个列表
    two, three, five = [1], [1], [1]
    i, j, k = 0, 0, 0
    while n > 0:
        now = min(two[i], three[j], five[k])
        two.append(now * 2)
        three.append(now * 3)
        five.append(now * 5)
        if now == two[i]:
            i += 1
        if now == three[j]:
            j += 1
        if now == five[k]:
            k += 1
        n -= 1
        if not n:
            return now

print hamming(1)
print hamming(2)
print hamming(3)
print hamming(100)
print hamming(4900)
print hamming(5000)


