function GetSum( a,b )
{
  var sum = Math.max(a, b);
  for(var i = Math.min(a, b); i < Math.max(a, b); i++) {
	  sum += i;
  }
  return sum;
}