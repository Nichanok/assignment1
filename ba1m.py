Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 05:52:31) 
[GCC 4.2.1 Compatible Apple LLVM 6.0 (clang-600.0.57)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> numbertosymbol = {0:'A', 1:'C', 2:'G', 3:'T'}
>>> def numbertopattern(n, k):
	if k == 1:
		return numbertosymbol[n]
	prefixindex = n//4
	r = n % 4
	symbol = numbertosymbol[r]
	prefixpattern = numbertopattern(prefixindex, k-1)
	return prefixpattern + symbol

>>> 
>>> print(numbertopattern(45, 4))
AGTC
>>> print(numbertopattern(8043, 11))
AAAACTTCGGT
>>> 
