# (151ms)
def move_zeros(array):
	ans = []
	for num in array:
		if num != 0 or isinstance(num, bool):
			ans.append(num)
	return ans + [0] * (len(array) - len(ans))

# (101ms)	
def move_zeros2(array):
	return filter(lambda x : x != 0 or isinstance(x, bool), array) + [0] * len(filter(lambda x : x == 0 and not isinstance(x, bool)))
	
print move_zeros2([9,0.0,0,9,1,2,0,1,0,1,0.0,3,0,1,9,0,0,0,0,9])
print move_zeros([False,1,0,1,2,0,1,3,"a"])