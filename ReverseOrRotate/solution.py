# (342ms)
def revrot(string, sz):
	if not string or sz <= 0 or sz > len(string):
		return ''
	chunks = [string[i * sz : i * sz + sz] for i in range(len(string) / sz)]
	for i, chunk in enumerate(chunks):
		count = 0
		for c in chunk:
			if int(c) % 2 != 0:
				count += 1
		chunks[i] = chunk[1:] + chunk[0] if count % 2 != 0 else chunk[::-1]
	return ''.join(chunks)
	
print revrot("123456987654", 6)
print revrot("66443875", 4)