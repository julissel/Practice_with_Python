'''
Given a positive integer "n" written as abcd... (a, b, c, d... being digits) and a positive integer "p".
Find a positive integer "k", if it exists, such as the sum of the digits of "n" taken to the successive powers
of "p" is equal to k * n.
Is there an integer "k" such as : (a ^ p + b ^ (p+1) + c ^(p+2) + d ^ (p+3) + ...) = n * k

If it is the case we will return "k", if not return -1.
'''

def dig_pow(n, p):
    list_numb = list(str(n))
    sum_total = sum([pow(int(list_numb[i]), (i + p)) for i in range(len(list_numb))])
    if sum_total % n == 0:
        return sum_total//n
    else:
        return -1
