# Python内置了Base64编解码的模块
from base64 import b64encode, b64decode
# (84ms)
# 标准是需要添加‘=’的，但是这道题目不允许添加等号
def to_base_64(string):
	trans = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
	binary = ''.join([to_bin(c) for c in string])
	equal = 3 - (len(binary) / 8) % 3
	if equal != 3:
		binary += ('0' * 8) * equal
	res = ''
	for i in range(len(binary) / 6):
		res += trans[int(binary[i * 6 : i * 6 + 6], 2)]
	return res[:-equal] + '=' * equal if equal != 3 else res

def to_bin(s):
	if isinstance(s, str):
		res = bin(ord(s))[2:]
		return '0' * (8 - len(res)) + res
	else:
		res = bin(s)[2:]
		return '0' * (6 - len(res)) + res

def from_base_64(string):
	trans = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
	binary = ''.join([to_bin(trans.find(c)) for c in string if c != '='])
	res = ''
	for i in range(len(binary) / 8):
		res += chr(int(binary[i * 8 : i * 8 + 8], 2))
	return res

# 以下是使用Python内置的模块中方法完成操作
def to_base_64_2(string):
    return b64encode(string).replace("=", '')
    
def from_base_64_2(string):
    return b64decode(string + "==")


print to_base_64('A')
print to_base_64('this is a string!!')
print from_base_64('QQ==')
print from_base_64('dGhpcyBpcyBhIHN0cmluZyEh')