//注意javascript的“/”运算符不是整除，所以需要使用Math.floor进行转换。
function score( dice ) {
  var count = new Array(7);
  count.fill(0);
  dice.forEach(function(item, array) {
    count[item]++;
  });
  var res = 0;
  for(var i = 2; i <= 6; i++) {
    res += Math.floor(count[i] / 3) * i * 100;
  }
  return res + Math.floor(count[1]/3)*1000 + count[1]%3*100 + count[5]%3*50;
}