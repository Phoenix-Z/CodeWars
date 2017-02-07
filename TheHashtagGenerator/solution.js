// (359ms)
function generateHashtag (str) {
	if(str == '') {
		return false;
	}
	res = '#';
	str.split(' ').forEach(function(item){
		if(item.length > 0)
			res += item[0].toUpperCase() + item.slice(1);
	})
	if(res.length > 140) {
		return false;
	} else {
		return res;
	}
}