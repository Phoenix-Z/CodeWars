import java.util.*;
/**
* (3405ms)
*/
public class Hamming {

	public static long hamming(int n) {
		public static long hamming(int n) {
		List<Long> two = new ArrayList<Long>();
		two.add(1L);
		List<Long> three = new ArrayList<Long>();
		three.add(1L);
		List<Long> five = new ArrayList<Long>();
		five.add(1L);
		int i = 0, j = 0, k = 0;
		while (n > 0) {
			long now = Math.min(two.get(i), Math.min(three.get(j), five.get(k)));
			two.add(now * 2);
			three.add(now * 3);
			five.add(now * 5);
			if(now == two.get(i)) {
				i++;
			}
			if(now == three.get(j)) {
				j++;
			}if(now == five.get(k)) {
				k++;
			} 
			if(--n == 0) {
				return now;
			}
		}
		return 0L;
	}
	}
  
}