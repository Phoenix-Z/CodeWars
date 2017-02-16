function removeZeros(array) {
	// 这里需要设置一个哨兵，否则会陷入死循环
	var limit = array.length;
	var i = 0;
	while(i < limit) {
		if(array[i] === 0 || array[i] === '0') {
			var tmp  = array[i];
			for(var j = i + 1; j < array.length; j++) {
				array[j - 1] = array[j];
			}
			array[array.length - 1] = tmp;
			limit--;
		} else {
			i++;
		}
	}
	return array;
}
