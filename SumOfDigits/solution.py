def digital_root(n):
	while len(`n`) == 1:
		n = sum([int(digit) for digit in `n`])
	return n
	
def digital_root2(n):
    return n if n < 10 else digital_root(sum(map(int,str(n))))