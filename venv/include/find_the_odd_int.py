'''
Given an array, find the integer that appears an odd number of times.
There will always be only one integer that appears an odd number of times.
'''

def find_it(seq):
    set_seq = set(seq)
    result_number = [k for k in {i: seq.count(i) for i in set_seq if seq.count(i) % 2 != 0 }.keys()]
    return result_number[0]
