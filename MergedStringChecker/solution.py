import collections


# (33ms)
# 这个做法首先判断s出现的字符以及字符出现的次数是否是part1和part2之和，然后分别探查
# 字符出现的顺序是否与s中的一致。
def is_merge(s, part1, part2):
    dt = collections.Counter(s)
    for key, value in dt.items():
        if part1.count(key) + part2.count(key) != value:
            return False
    i = j = k = 0
    while i < len(s) and j < len(part1):
        if s[i] == part1[j]:
            j += 1
        i += 1
    i = 0
    while i < len(s) and k < len(part2):
        if s[i] == part2[k]:
            k += 1
        i += 1
    if j != len(part1) or k != len(part2):
        return False
    return True


# (121ms)
# 这是一个递归的做法，比较好的一个做法。
def is_merge2(s, part1, part2):
    if not part1:
        return s == part2
    if not part2:
        return s == part1
    if not s:
        return part1 + part2 == ''
    if s[0] == part1[0] and is_merge(s[1:], part1[1:], part2):
        return True
    if s[0] == part2[0] and is_merge(s[1:], part1, part2[1:]):
        return True
    return False


print is_merge('codewars', 'cdw', 'oears')
print is_merge('codewars', 'code', 'wars')
print is_merge('codecars', 'code', 'cars')
print is_merge2('codewars', 'cod', 'wars')
print is_merge2('bananas', 'bans', 'ana')
