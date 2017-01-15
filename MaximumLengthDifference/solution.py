# (161ms)
def mxdiflg(a1, a2):
	return max(max(map(len, a1)) - min(map(len, a2)), 
	max(map(len, a2)) - min(map(len, a1))) if a1 and a2 else -1

# (178ms)	
def mxdiflg2(a1, a2):
	return max([abs(len(x) - len(y)) for x in a1 for y in a2]) if a1 and a2 else -1