// (302ms)
function array_diff(a, b) {
  return a.filter(x => b.indexOf(x) == -1)
  //或者使用includes方法
  //return a.filter(x => !b.includes(x))
}