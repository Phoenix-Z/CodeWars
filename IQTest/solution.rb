# (231ms)
def iq_test(numbers)
  ans = numbers.split(' ').collect {|x| x.to_i & 1}
	if ans.index(0) == ans.rindex(0)
		return ans.index(0) + 1
	else 
    return ans.index(1) + 1
  end
end