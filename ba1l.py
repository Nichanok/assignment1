symboltonumber = {'A':0, 'C':1, 'G':2, 'T':3}
def PatternToNumber(pattern):
	n = len(pattern)
	if n == 0:
		return 0
	elif n == 1:
		return symboltonumber[pattern]
	else:
		return 4*PatternToNumber(pattern[:-1]) + symboltonumber[pattern[-1]]

print(PatternToNumber("GTTTATGCGCAAGCCGCGTA"))
