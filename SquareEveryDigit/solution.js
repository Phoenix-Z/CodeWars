// (305ms)
function squareDigits(num){
  return Number(num.toString().split('').map(Number).map(x => x * x).join(''))
}