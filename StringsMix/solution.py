# coding:utf-8
# 这个题目难度不大，需要注意如何精简Python代码。
def mix(s1, s2):
	ans = []
	for letter in 'abcdefghijklmnopqrstuvwxyz':
		# 多个变量赋值，可以使用tuple来实现，而不需要写多行
		count1, count2 = s1.count(letter), s2.count(letter)
		if max(count1, count2) > 1:
			prefix = '1' if count1 > count2 else '2' if count2 > count1 else '='
			ans.append(prefix + ':' + letter * max(count1, count2))
	# 注意如何定义排序的策略，s表示list中的一个元素，而后面跟着一个tuple
	# Python先根据第一个策略排序，如果相等，再根据第二个策略排序
	return '/'.join(sorted(ans, key = lambda s : (-len(s), s)))

s1 = "my&friend&Paul has heavy hats! &"
s2 = "my friend John has many many friends &"	
print mix(s1, s2)