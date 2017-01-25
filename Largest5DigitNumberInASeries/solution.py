def solution(digits):
	max_val = 0
	dig = str(digits)
	for i in xrange(len(dig) - 5 + 1):
		max_val = max(max_val, int(dig[i : i + 5]))
	return max_val
	
def solution2(digits):
	return max([int(digits[i : i + 5]) for i in xrange(len(digits) - 4)])
	
print solution(123456)
print solution2('123456')
