# coding:utf-8
from re import split, escape


def solution(string, markers):
    strs = string.split('\n')
    for index, s in enumerate(strs):
        for marker in markers:
            if s.find(marker) >= 0:
                strs[index] = strs[index][:s.find(marker)]
        strs[index] = strs[index].rstrip()
    return '\n'.join(strs)


def solution2(string, markers):
    if markers:
        pattern = "[" + escape("".join(markers)) + "]"
    else:
        pattern = ''
    # 划分行可以直接使用splitlines方法
    return '\n'.join(split(pattern, line)[0].rstrip() for line in string.splitlines())


print solution("a #b\nc\nd $e f g", ["#", "$"])
print solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])
