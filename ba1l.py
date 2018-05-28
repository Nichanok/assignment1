Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 05:52:31) 
[GCC 4.2.1 Compatible Apple LLVM 6.0 (clang-600.0.57)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> symb_to_numb = {'A':0, 'C':1, 'G':2, 'T':3}

>>> def patterntonumber(pattern)
SyntaxError: invalid syntax
>>> def patterntonumber(pattern):
	if not pattern:
		return 0
	return 4*patterntonumber(pattern[:-1]) + symb_to_numb[pattern[-1]]
if __name__ == "__main__":
    print pattern_to_number("ATGTCAAGGGGTGACGAAAGGTAGGTTG")
    
SyntaxError: invalid syntax
>>> ef patterntonumber(pattern):
	if not pattern:
		return 0
	return 4*patterntonumber(pattern[:-1]) + symb_to_numb[pattern[-1]]
SyntaxError: invalid syntax
>>> def patterntonumber(pattern):
	if not pattern:
		return 0
	return 4*patterntonumber(pattern[:-1]) + symb_to_numb[pattern[-1]]

>>> if __name__ == "__main__":
	 print patterntonumber("AGT")
	 
SyntaxError: invalid syntax
>>> def patterntonumber(pattern):
	if not pattern:
		return 0
	return 4*patterntonumber(pattern[:-1]) + symb_to_numb[pattern[-1]]

>>> if __name__ == "__main__":
	 print patterntonumber(AGT)
	 
SyntaxError: invalid syntax
>>> def patterntonumber(pattern):
	if not pattern:
		return 0
	symbol = lastsymbol(pattern)
	prefix= prefix(pattern)
	return 4*patterntonumber(prefix)+symbol_to_numb(symbol)
print(patterntonumber(AGT))
SyntaxError: invalid syntax
>>> def patterntonumber(pattern):
	if not pattern:
		return 0
	symbol = lastsymbol(pattern)
	prefix= prefix(pattern)
	return 4*patterntonumber(prefix)+symbol_to_numb(symbol)
print(patterntonumber("AGT"))
SyntaxError: invalid syntax
>>> def patterntonumber(pattern):
	if not pattern:
		return 0
	symbol = lastsymbol(pattern)
	prefix= prefix(pattern)
	return 4*patterntonumber(prefix)+symbol_to_numb(symbol)
print patterntonumber(AG)
SyntaxError: invalid syntax
>>> def patterntonumber(pattern):
	if not pattern:
		return 0
	symbol = lastsymbol(pattern)
	prefix= prefix(pattern)
	return 4*patterntonumber(prefix)+symbol_to_numb(symbol)
print patterntonumber("AG")
SyntaxError: invalid syntax
>>> print(symbol_to_numb)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    print(symbol_to_numb)
NameError: name 'symbol_to_numb' is not defined
>>> symb_to_numb = {'A':0, 'C':1, 'G':2, 'T':3}
>>> print(symb_to_numb)
{'A': 0, 'C': 1, 'G': 2, 'T': 3}
>>> def patterntonumber(pattern):
	if not pattern:
		return 0
	symbol = lastsymbol(pattern)
	prefix= prefix(pattern)
	return 4*patterntonumber(prefix)+symb_to_numb(symbol)
print(patterntonumber("ATG")
      
SyntaxError: invalid syntax
>>> print(symb_to_number("A"))
      
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    print(symb_to_number("A"))
NameError: name 'symb_to_number' is not defined
>>> print(symb_to_numb("A"))
      
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    print(symb_to_numb("A"))
TypeError: 'dict' object is not callable
>>> symb_to_numb = {'A':0, 'C':1, 'G':2, 'T':3}
      
>>> print(symb_to_numb('A'))
      
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    print(symb_to_numb('A'))
TypeError: 'dict' object is not callable
>>> def patterntonumber(pattern):
	if not pattern:
		return 0
	symbol = lastsymbol(pattern)
	prefix= prefix(pattern)
	return 4*patterntonumber(prefix)+symb_to_numb(symbol)
      pattern="AGT"
      
SyntaxError: unindent does not match any outer indentation level
>>> pattern = AGT
      
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    pattern = AGT
NameError: name 'AGT' is not defined
>>> print(patterntonumber("ATG"))
      
14
>>> print(patterntonumber("TTGATGTTGAATGGAGCCAGCTCTT"))
      
1094830357301727
>>> symb_to_numb = {'A':0, 'C':1, 'G':2, 'T':3}
      
>>> def patterntonumber(pattern):
	if not pattern:
		return 0
	symbol = lastsymbol(pattern)
	prefix= prefix(pattern)
	return 4*patterntonumber(prefix)+symb_to_numb(symbol)
      print(patterntonumber("TTGATGTTGAATGGAGCCAGCTCTT"))
      
SyntaxError: unindent does not match any outer indentation level
>>> def patterntonumber(pattern):
	if not pattern:
		return 0
	symbol = lastsymbol(pattern)
	prefix= prefix(pattern)
	return 4*patterntonumber(prefix)+symb_to_numb(symbol)

      
>>> print(patterntonumber("TTGATGTTGAATGGAGCCAGCTCTT"))
      
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    print(patterntonumber("TTGATGTTGAATGGAGCCAGCTCTT"))
  File "<pyshell#41>", line 4, in patterntonumber
    symbol = lastsymbol(pattern)
NameError: name 'lastsymbol' is not defined
>>> print(patterntonumber("ACAACTATTTTCCGAGATCAATAATCG"))
      
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    print(patterntonumber("ACAACTATTTTCCGAGATCAATAATCG"))
  File "<pyshell#41>", line 4, in patterntonumber
    symbol = lastsymbol(pattern)
NameError: name 'lastsymbol' is not defined
>>> print(patterntonumber("TTGATGTTGAATGGAGCCAGCTCTT"))
      
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    print(patterntonumber("TTGATGTTGAATGGAGCCAGCTCTT"))
  File "<pyshell#41>", line 4, in patterntonumber
    symbol = lastsymbol(pattern)
NameError: name 'lastsymbol' is not defined
>>> print(patterntonumber("ATG"))
      
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    print(patterntonumber("ATG"))
  File "<pyshell#41>", line 4, in patterntonumber
    symbol = lastsymbol(pattern)
NameError: name 'lastsymbol' is not defined
>>> 
