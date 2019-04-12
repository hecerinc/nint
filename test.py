# import sys
# sys.path.append("C:/dev/compiler")
# from icg import *
from icg.Expr import Expr
from icg.Arith import Arith



exp1 = Expr(1, 'INT')
exp2 = Expr(2, 'INT')
a = Arith('+', exp1, exp2)
print(a.toString())
