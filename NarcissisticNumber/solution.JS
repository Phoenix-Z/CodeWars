// (293ms)
function narcissistic( value ) {
  var sum = 0;
  var strValue = value.toString();
  for(var i = 0; i < strValue.length; i++) {
	  sum += Math.pow(Number(strValue[i]), strValue.length);
  }
  return sum == value;
}

// (307ms)
function narcissistic( value ) {
  return ('' + value).split('').reduce(function(p, c){
    return p + Math.pow(c, ('' + value).length)
    }, 0) == value;
}