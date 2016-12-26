# -*- coding: utf-8 -*-
# 解题思路见链接：http://stackoverflow.com/questions/9368205/given-a-number-find-the-next-higher-number-which-has-the-exact-same-set-of-digi
# 可分为以下几个步骤来找到所需的数字
# Step1.首先将这个数字分成两个部分，后半部分是降序排列的，那么后半部分就不会存在一个数字使用相同
#		的digits，且比这个数字大。
# Step2.选取前半部分的最后一个元素x，然后在后半部分中找到一个比x大的最小的数字，并交换他们，这时
#		这个数字已经比原始数字大了。
# Step3.对后半部分进行排序，使这部分的数字从小到大排列，最后将前后两个部分拼接在一起，所得的结果就
#		是比原始数字大的下一个数字
def next_bigger(n):
	#your code here
	n_str = list(`n`)
	i = len(n_str) - 1
	while i > 0 and n_str[i] <= n_str[i - 1]:
		i -= 1
	if i == 0:
		return -1
	j = i
	while j < len(n_str) and n_str[j] > n_str[i - 1]:
		j += 1
	n_str[i - 1], n_str[j - 1] = n_str[j - 1], n_str[i - 1]
	remain = n_str[i:]
	remain.sort()
	return int(''.join(n_str[:i] + remain))
		
print next_bigger(2017)