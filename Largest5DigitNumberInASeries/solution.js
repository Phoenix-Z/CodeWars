function solution(digits){
  var maxVal = 0;
  for(var i = 0; i < digits.length - 4; i++) {
	  maxVal = Math.max(maxVal, Number(digits.slice(i, i + 5)))
  }
  return maxVal;
}