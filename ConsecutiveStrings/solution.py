#题意错误理解一，意味返回的是最长的k个字符串，这里需要注意的是对原始的数据去重
#可以先用set去重，再将其转化为list
def longest_consec_not_correct(strarr, k):
	if not (0 < k <= len(strarr)):
		return ''
	# 注意这句
	sortedarr = list(set(strarr))
	
	sortedarr.sort(key = lambda x : -len(x))
	sortedarr = sortedarr[:k] 
	#由于经过set的操作，数据变得无序，如果需要保持原始数组中数据的相对顺序，可以像下面这句写的一样
	sortedarr.sort(key = strarr.index)
	return ''.join(sortedarr)
	
#题意理解错误二，以为是对字符串长度排序，每一种长度只返回其中一个元素，这里使用了类似
#桶排序的思想
def longest_consec_not_correct2(strarr, k):
	if not (0 < k <= len(strarr)):
		return ''
	bucket = {}
	for string in strarr:
		key = len(string)
		if key not in bucket:
			bucket[key] = []
		bucket[key].append(string)
	ans = []
	print bucket
	for v in [bucket[key] for key in sorted(bucket.keys())[::-1]]:
		v.sort()
		ans.append(v[0])
		if len(ans) == k:
			break
	ans.sort(key = strarr.index)
	return ''.join(ans)
		
# (747ms)	
#正确的题意是：返回由在数组中取的k个连续字符串组成的第一个最长的字符串
def longest_consec(strarr, k):
	if not (0 < k <= len(strarr)):
		return ''
	cons = []
	for i in range(len(strarr) - k + 1):
		cons.append(''.join(strarr[i : i+k]))
	#sort方法可以指定reverse参数为True,就可以逆序排序
	#cons.sort(key = lambda x : len(x), reverse = True)
	#return cons[0]
	#由于在Python中函数也是一个对象，可以直接把len函数对象赋值给key，就不需要自己定义匿名函数了
	#return sorted(cons, key = len, reverse = True)[0]
	#由于只是需要最长的字符串，使用max函数即可，不要进行排序
	return max(cons, key = len)

#思想是一样，但是代码非常简洁	
def longest_consec2(s, k):
    return max(["".join(s[i:i+k]) for i in range(len(s)-k+1)], key=len) if s and 0 < k <= len(s) else ""
	

print longest_consec(["zone", "abigail", "theta", "form", "libe", "zas", "theta", "abigail"], 2)
print longest_consec(["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 3)
print longest_consec(["itvayloxrp","wkppqsztdkmvcuwvereiupccauycnjutlv","vweqilsfytihvrzlaodfixoyxvyuyvgpck"], 2)