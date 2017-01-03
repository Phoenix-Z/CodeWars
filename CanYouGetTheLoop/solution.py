# coding=utf-8
#(270ms)
#这个方法是将链表的所有不同的节点放到一个set中，一旦发现某个节点已经在set中时，
#就说明这个节点是环的头，然后将set中所有节点个数减去不在环内的节点的个数即可。
def loop_size(node):
	now = node
	exist = set()
	while now not in exist:
		exist.add(now)
		now = now.next
	tail = 0
	while node != now:
		node = node.next
		tail += 1
	return len(exist) - tail

#(286ms)	
#这个方法是使用两个指针，一个走一步，一个走两步，一旦两个指针相遇，一定是在环中，
#然后固定一个指针，另一个指针再走一圈即可知道环的长度是多少了。
def loop_size(node):
    turtle, rabbit = node.next, node.next.next
    
    while turtle != rabbit:
        turtle = turtle.next
        rabbit = rabbit.next.next
  
    count = 1
    rabbit = rabbit.next
    while turtle != rabbit:
        count += 1
        rabbit = rabbit.next

    return count