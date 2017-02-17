// (1268ms)
function hamming (n) {
   var two = [1], three = [1], five = [1];
   while(n > 0) {
	   now = Math.min(two[0], three[0], five[0]);
	   two.push(now * 2);
	   three.push(now * 3);
	   five.push(now * 5);
	   if(now == two[0]) {
		   two.shift();
	   }
	   if(now == three[0]) {
		   three.shift();
	   }
	   if(now == five[0]) {
		   five.shift();
	   }
	   if(--n == 0) {
		   return now;
	   }
   }
}