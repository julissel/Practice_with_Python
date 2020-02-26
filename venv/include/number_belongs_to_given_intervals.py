"""
There are given intervals {-10}and(-5, 3]and(8, 12)and[16, infinity).
The program returns 'True' if the number belongs to any of interval's part? and 'False' if it not.
"""
numb = int(input())
print((-10 == numb)or(-5 < numb <= 3)or(8 < numb < 12)or(numb >= 16))
