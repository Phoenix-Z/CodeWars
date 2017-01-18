# (150ms)
def array_diff(a, b):
	for num in b:
		while num in a:
			a.remove(num)
	return a

# (199ms)	
def array_diff2(a, b):
    return [x for x in a if x not in b]