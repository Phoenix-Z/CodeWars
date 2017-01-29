//(394ms)
function removeNb (n) {
	sum = n * (n + 1) / 2;
	res = Array();
	for(var i = 1; i <= n; i++) {
		if((sum - i) % (i + 1) == 0 && (sum - i) / (i + 1) <= n) {
			res.push([i, (sum - i) / (i + 1)]);
		}
	}
	return res;
}