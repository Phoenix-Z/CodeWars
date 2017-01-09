# 这是个整数分拆的题目，详细解释见维基百科
# https://zh.wikipedia.org/wiki/%E6%95%B4%E6%95%B8%E5%88%86%E6%8B%86
def exp_sum(n):
	if n < 0:
		return 0
	ans = [1] * (n + 1)
	for i in range(2, n + 1):
		for j in range(i, n + 1):
			ans[j] += ans[j - i]
	return ans[n]

		
print exp_sum(0)
print exp_sum(1)
print exp_sum(2)
print exp_sum(3)
print exp_sum(4)
print exp_sum(50)