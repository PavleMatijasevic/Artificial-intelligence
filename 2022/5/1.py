import copy
from itertools import combinations
class Formula:
    def __init__(self):
        self.components = []
    
    def interpret(self, valuation):
        pass
    
    def __repr__(self):
        return str(self)

    def __eq__(self,rhs):
        return Eq(self.copy(),rhs.copy())
    def __and__(self,rhs):
        return And(self.copy(), rhs.copy())
    def __or__(self, rhs):
        return Or(self.copy(), rhs.copy())
    def __invert__(self):
        return Not(self.copy())
    def __rshift__(self, rhs):
        return Impl(self.copy(), rhs.copy())
    
    def copy(self):
        return copy.deepcopy(self)

    def get_all_variables(self):
        result = set()
        for c in self.components:
            result.update(c.get_all_variables())
        return result
    def je_valjana(self): # u svakoj val. tacna
        promenljive = list(self.get_all_variables())
        for valuation in all_valuations(promenljive):
            if self.interpret(valuation) == False:
                return False, valuation
            return True, None
    
    def je_kontradikcija(self): # u svim val. netacna
        promenljive = list(self.get_all_variables())
        for valuation in all_valuations(promenljive):
            if self.interpret(valuation) == True:
                return False, valuation
            return True, None
            
    def je_poreciva(self): # postoji jedna netacna val
        promenljive = list(self.get_all_variables())
        for valuation in all_valuations(promenljive):
            if self.interpret(valuation) == False:
                return True, valuation
            return False, None

    def je_zadovoljiva(self): # postoji jedna val u kojoj je tacna
        promenljive = list(self.get_all_variables())
        for valuation in all_valuations(promenljive):
            if self.interpret(valuation) == True:
                return True, valuation
            return False, None
    
class Var(Formula):
    
    def __init__(self, name):
        super().__init__()
        self.name = name
    
    def interpret(self, valuation):
        return valuation[self.name]

    def __str__(self):
        return self.name
    
    def get_all_variables(self):
        return set([self.name])

class Const(Formula):
    def __init__(self, value):
        super().__init__()
        self.value = value
    
    def interpret(self, valuation):
        return self.value
    
    def __str__(self):
        return "{}".format(1 if self.value else 0)

class And(Formula):
    def __init__(self,lhs,rhs):
        super().__init__()
        self.components = [lhs,rhs]
    
    def interpret(self, valuation):
        return self.components[0].interpret(valuation) and self.components[1].interpret(valuation)
    
    def __str__(self):
        return f"({self.components[0]}) & ({self.components[1]})"
class Or(Formula):
    def __init__(self, lhs, rhs):
        super().__init__()  
        self.components = [lhs,rhs]  
    def interpret(self, valuation):
        return self.components[0].interpret(valuation) or self.components[1].interpret(valuation)
    def __str__(self):
        return f"({self.components[0]}) | ({self.components[1]})"
class Impl(Formula):
    def __init__(self, lhs, rhs):
        super().__init__()
        self.components = [lhs, rhs]
    def interpret(self, valuation):
        return not self.components[0].interpret(valuation) or self.components[1].interpret(valuation) 
    def __str__(self):
        return f"({self.components[0]}) >> ({self.components[1]})"

class Eq(Formula):
    def __init__(self, lhs, rhs):
        super().__init__()
        self.components = [lhs,rhs]
    
    def interpret(self, value):
        return self.components[0].interpret(valuation) == self.components[1].interpret(valuation)
    
    def __str__(self):
        return f"({self.components[0]}) == ({self.components[1]})"

class Not(Formula):
    def __init__(self, operand):
        super().__init__()
        self.components = [operand]
    def interpret(self, valuation):
        return not self.components[0].interpret(valuation)
    def __str__(self):
        return f"~({self.components[0]})"

def vars(names):
    return [Var(name.strip()) for name in names.split(',')]

def evaluate_formula(formula):
    print(formula)
    print("valjana: ", formula.je_valjana())
    print("zadovoljiva: ", formula.je_zadovoljiva())
    print("poreciva: ", formula.je_poreciva())
    print("kontradikcija: ", formula.je_kontradikcija())
    for val in all_valuations(formula.get_all_variables()):
        if formula.interpret(val):
            print(val)

def all_valuations(variables):
    for r in range(len(variables)+1):
        for true_variables in combinations(variables,r):
            result = {x:False for x in variables}
            result.update({x:True for x in true_variables})
            yield result




if __name__ == '__main__':
 
 
   """
   ## prvi zadatak
   x,y,z = vars("x,y,z")
   formula = x | ~x
   valuation = {
       "x":True,
       "y":False,
       "z": True
   }
   evaluate_formula(formula)
   """

'''
## drugi:
U igri mines dimenzija 2x3 dobijena je sledeca konfiguracija
|1|A|C|
|1|B|2|
A,B,C su neotvorena polja, a brojevi oznacavaju broj mina u okolnim poljima.
Zapisati u iskaznoj logici uslove koji moraju da vaze.
'''

"""
A, B, C = vars("A, B, C")
formula = (A | B) & ~(A & B) & (B | A) & ~(B & A) \
    & ~(A & B & C) & ~(~A & ~B & ~C)\
    & (A | B) & (A | C) & (B | C)
evaluate_formula(formula)
"""



'''
#treci
Date su dve kutije A,B robot mora da stavi 
objekat u tacno jednu od njih.
'''
"""
A, B = vars("A, B")
formula = ~(A & B) & (A | B) & ~(~A & ~B)
evaluate_formula(formula)
"""



''' 
|A|B|
|C|D|
Zapisati uslov da se u tabeli 2x2 sa poljima A,B,C,D
moze postaviti tacno jedan zeton u 
svakom redu
'''

"""
A,B,C,D = vars("A,B,C,D")
formula = (A | B) & ~(A & B) & ~(~A & ~B) \
    & (C | D) & ~(C & D) & ~(~C & ~D)
evaluate_formula(formula)
"""


'''
U iskaznoj logici zapisati uslov
da bitovi 3-bitnog polja moraju biti jednaki
'''

"""
A,B,C = vars("A,B,C")
formula = (A == B) & (B == C)
evaluate_formula(formula)
"""

'''
U iskoznoj logici zapisati da je 4 bitna reprezentacija broja palindrom ali da 
bitovi nisu jednaki
ABCD
'''
"""
A,B,C,D = vars("A,B,C,D")
formula = (A == D) & (B == C) & ~(A == B & B == C & C == D)
evaluate_formula(formula)

"""



