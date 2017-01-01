#(121ms)
import re
def is_valid_IP(string):
	strs = string.split('.');
	if len(strs) != 4:
		return False
	for s in strs:
		match_obj = re.match('^([1-9][0-9]{0,2}$)|^0$', s)
		if not match_obj or not 0 <= int(s) < 256:
			return False
	return True
	
print is_valid_IP('12.255.56.0')
print is_valid_IP('abc.def.ghi.jkl')
print is_valid_IP('123.456.789.0')
print is_valid_IP('12.34.56.-1')
print is_valid_IP('123.045.067.089')
print is_valid_IP('12.34.56   .1')
print is_valid_IP('1.2.3.4 ')