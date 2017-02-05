// (316ms)
// 使用的是递归的做法。
function isMerge(s, part1, part2) {
	if(part1.length == 0) {
		return s == part2;
	}
	if(part2.length == 0) {
		return s == part1;
	}
	if(s.length == 0) {
		return part1 + part2 == '';
	}
	if(s[0] == part1[0] && isMerge(s.slice(1), part1.slice(1), part2))
		return true;
	if(s[0] == part2[0] && isMerge(s.slice(1), part1, part2.slice(1)))
		return true;
	return false;
}