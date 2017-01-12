# 这是一个动态规划求取连续子数组的最大和问题。
# curMax[i]表示以arr[i]结尾的子数组的最大子段和，即curMax[i]=max{sum(arr[j~k])},其中0<=j<=i，j<=k<=i。
# 那么对于数组arr[0~n]的最大子段和为max{curMax[i]}，其中0<=i<n。
# 所以动态规划的条件是curMax[i] = max{ curMax[i-1]+arr[i]，arr[i]}
def maxSequence(arr):
	if not arr:
		return 0
	curMax = [arr[0]]
	for i in range(1, len(arr)):
		curMax.append(max(curMax[i - 1] + arr[i], arr[i]))
	return max(curMax)
	
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print maxSequence(arr)
