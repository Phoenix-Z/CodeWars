def find_it(seq):
    '''Find the only one number which appears an odd number of times.
    
    Use xor operation to find it. Because x ^ x = 0 and x ^ 0 = x'''
    ans = 0
    for num in seq:
        ans ^= num
    return ans