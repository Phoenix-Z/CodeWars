function sumStrings(a,b) { 
	var ans = [];
	var i =a.length - 1 , j = b.length - 1;
	var addOne = false;
	while(i >= 0 && j >= 0) {
		var numA = Number(a[i]);
		var numB = Number(b[j]);
		var sum = addOne ? numA + numB + 1 : numA + numB;
		if(sum >= 10) {
			ans.push((sum % 10).toString());
			addOne = true;
		} else {
			ans.push(sum.toString());
			addOne = false;
		}
		i--;
		j--;
	}
	while(i >= 0) {
		sum = addOne ? Number(a[i]) + 1 : Number(a[i]);
		if(sum >= 10) {
			ans.push((sum % 10).toString());
			addOne = true;
		} else {
			ans.push(sum.toString());
			addOne = false;
		}
		i--;
	}
	while(j >= 0) {
		sum = addOne ? Number(b[j]) + 1 : Number(b[j]);
		if(sum >= 10) {
			ans.push((sum % 10).toString());
			addOne = true;
		} else {
			ans.push(sum.toString());
			addOne = false;
		}
		j--;
	}
	if(addOne) {
		ans.push('1');
	}
	while(ans[ans.length - 1] == '0') {
		ans.pop();
	}
	return ans.reverse().join('');
}