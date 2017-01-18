# (172ms)
def square_digits(num):
	return int(''.join([`int(s)**2` for s in `num`]))