function findOdd(A) {
  var ans = 0;
  for(var i = 0; i < A.length; i++) {
    ans ^= A[i];
  }
  return ans;
}