// (518ms)
//该方法与Python的解法是一样的。
function dblLinear(n) {
	var doubleArr = [1];
	var tribleArr = [1];
	var i = 0, j = 0;
	while(true) {
		var num = Math.min(doubleArr[i], tribleArr[j]);
		doubleArr.push(2 * num + 1);
		tribleArr.push(3 * num + 1);
		if(n == 0) {
			return num;
		}
		if(num == doubleArr[i]) {
			i++;
		}
		if(num == tribleArr[j]) {
			j++;
		}
		n--;
	}
}