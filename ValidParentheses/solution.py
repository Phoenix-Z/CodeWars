# using list as stack to solve it
def valid_parentheses(string):
    #your code here
	stack = []
	for char in string:
		if char == '(':
			stack.append(char)
		elif char == ')':
			if not stack:
				return False
			else:
				stack.pop()
	if stack:
		return False
	return True

print valid_parentheses('(')