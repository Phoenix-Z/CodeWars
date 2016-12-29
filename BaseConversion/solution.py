def convert(input, source, target):
	conv = {'bin' : (2, '01'), 
			'oct' : (8, '01234567'), 
			'dec' : (10, '0123456789'), 
			'hex' : (16, '0123456789abcdef'),
			'allow' : (26, 'abcdefghijklmnopqrstuvwxyz'),
			'allup' : (26, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'),
			'alpha' : (52, 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'),
			'alphanum' : (62, '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
			}
	# decode
	base, pos = conv[source]
	num = 0
	for i in range(len(input))[::-1]:
		num += pos.find(input[i]) * (base ** (len(input) - i - 1))

	# encode
	base, pos = conv[target]
	ans = ''
	if num == 0:
		return pos[0]
	while num > 0:
		ans += pos[num % base]
		num //= base
	return ans[::-1]

	
print convert('hello', 'allow', 'hex')		#should return "320048"
print convert("15", 'dec', 'bin') 			#should return "1111"
print convert("15", 'dec', 'oct') 			#should return "17"
print convert("1010", 'bin', 'dec') 		#should return "10"
print convert("1010", 'bin', 'hex') 		#should return "a"
print convert("0", 'dec', 'alpha') 			#should return "a"
print convert("27", 'dec', 'allow') 		#should return "bb"
