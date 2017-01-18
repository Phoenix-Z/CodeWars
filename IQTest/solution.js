// (405ms)
// 注意numbers是一个字符串而不是一个数组
function iqTest(numbers){
	var arr = [Array(), Array()];
	numbers.split(' ').forEach(function(item, index, array) {
		arr[Number(item) & 1].push(index + 1);
	});
	if(arr[0].length == 1)
		return arr[0][0];
	return arr[1][0];
}