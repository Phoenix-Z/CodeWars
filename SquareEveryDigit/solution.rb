# (356ms)
def square_digits num
	return num.to_s.split('').collect {|x| x.to_i ** 2}.join.to_i
end