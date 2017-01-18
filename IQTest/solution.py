# (127ms)
def iq_test(numbers):
	arr = [[],[]]
	for index, num in enumerate(numbers.split(' ')):
		arr[int(num) & 1].append(index + 1)
	return arr[0][0] if len(arr[0]) == 1 else arr[1][0]

# (89ms)	
def iq_test2(numbers):
	arr = [int(num) & 1 for num in numbers.split(' ')]
	return arr.find(0) + 1 if arr.count(0) == 1 else arr.find(1) + 1