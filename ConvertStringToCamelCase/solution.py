def to_camel_case(text):
	strs = text.replace('_', '-').split('-')
	return strs[0] + ''.join(str.capitalize() for str in strs[1:])

print to_camel_case('the-stealth-warrior')
print to_camel_case('The_Stealth_Warrior')
print to_camel_case('The_Stealth-warrior')
