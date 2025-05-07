#
# Jason H. Wells - wellsjason543 at gmail dot com - jwellsuhhuh (Discord)
#

class Money:
    # Money('5.55', 4) --> '5.59' (self.inDollars) or 559 (self.inCents)
    def __init__(self, dollarsPortion: str, centsPortion: int = 0):   
        normalizedDollarsPortion = Money.normalizeDollarsFormatting(dollarsPortion)
        dollarsPortionInCents = Money.dollarsToCents(normalizedDollarsPortion)
        self.inCents = dollarsPortionInCents + centsPortion
        self.inDollars = Money.centsToNormalizedDollars(self.inCents)
    
    def __add__(self, other):
        resultInCents: int = self.inCents + other.inCents
        return Money('0', resultInCents)
    
    def __sub__(self, other):
        resultInCents: int = self.inCents - other.inCents
        return Money('0', resultInCents)

    def __repr__(self):
        return f'Money({self.inDollars})'
    
    @staticmethod
    def normalizeDollarsFormatting(rawDollars: str):
        dollars = str(rawDollars).strip('$')
        if '.' not in dollars:
            normalizedDollars = dollars + '.00'
        elif dollars[-1] == '.':
            normalizedDollars = dollars + '00'
        elif dollars[-2] == '.':
            normalizedDollars = dollars + '0'
        elif dollars[-3] == '.':
            normalizedDollars = dollars
        else:
            raise TypeError(f'Invalid Dollars Format: {rawDollars}')
        return normalizedDollars

    @staticmethod
    def dollarsToCents(dollars: str) -> int:
        # requires normalized dollars
        return int(dollars[:-3] + dollars[-2:])
    
    @staticmethod
    def centsToNormalizedDollars(cents: int) -> str:
        sign = 1
        if cents < 0:
            sign = -1 
            cents = abs(cents)
        
        dollarsPortion = str(sign * (cents // 100))
        centsPortion = str(cents % 100)
        if len(centsPortion) == 1:
            centsPortion = '0' + centsPortion # add leading zero
        return dollarsPortion + '.' + centsPortion

if __name__ == '__main__':
    print('Money module test:')
    a = Money('0')
    b = Money('$03.39', 40)
    c = Money('-50')
    d = b + c
    print(a,b,c,d)