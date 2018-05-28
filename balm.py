numb_to_symb = {0:'A', 1:'C', 2:'G', 3:'T'}
def numbertopattern(index, k):


    def numbertopattern(index, k):
      prefixindex = quotient(index,4)
      r = remainder(index,4)
      symbol = numb_to_symb(r)
      prefixpattern = numbertopattern(prefixindex, k-1)
      return prefixpattern
    index=45
    k=4
    print(numbertopattern(index,k))


def numberToPattern(number,k):
    if k == 1:
        return numberToSymbol(number)
    quotient, remainder = divmod(number,4)
    prefixPattern = numberToPattern(quotient,k-1)
    symbol = numberToSymbol(remainder)
    return prefixPattern+symbol
