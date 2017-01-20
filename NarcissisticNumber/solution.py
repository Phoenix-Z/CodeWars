# (131ms)
def narcissistic( value ):
	return sum([int(x) ** len(`value`) for x in `value`]) == value