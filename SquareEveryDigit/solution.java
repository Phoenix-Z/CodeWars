/**
 * (3594ms)
 */
import java.util.*;
public class SquareDigit {

  public int squareDigits(int n) {
    List<Integer> pow = new ArrayList<>();
	while(n > 0) {
		int digit = n % 10;
		pow.add(digit * digit);
		n = n / 10;
	}
	StringBuilder ans = new StringBuilder();
	for(int i = pow.size() - 1; i >= 0; i--) {
		ans.append(pow.get(i));
	}
	return Integer.parseInt(ans.toString());
  }

}