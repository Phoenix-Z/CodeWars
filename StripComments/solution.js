function solution(input, markers){
  var strs = input.split('\n');
  for(var i = 0; i < strs.length; i++) {
	  for(var j = 0; j < markers.length; j++) {
		  strs[i] = strs[i].split(markers[j])[0];
	  }
	  strs[i] = strs[i].trimRight();
  }
  return strs.join('\n');
}