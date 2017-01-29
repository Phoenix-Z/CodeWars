# coding:utf-8
# (342ms)
# 这个题目乍一看可以分别对a，b进行遍历，时间复杂度为O(n^2)，但是由于b可以直接通过a和n计算出来，所以只需要对a进行遍历，时间复杂度为O(n).
def removNb(n):
	sum = n * (n + 1) / 2
	return [(a, (sum + 1) / (a + 1) - 1) for a in range(1, n+1) if (sum + 1) % (a + 1) == 0 and (sum + 1) / (a + 1) - 1 <= n]
	
print removNb(100)
print removNb(26)
