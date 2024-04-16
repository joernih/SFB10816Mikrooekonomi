#######################################################################################
import sympy
## Import packages
import os
import json
import sympy
import numpy
from sympy import solve, Eq, symbols, latex, simplify
import pandas
import os
import rpy2
from rpy2 import robjects
#####################################################################################################################
beforems = set(dir())
############################################################################################
U_a, x_1, x_2, p_1, p_2, m= sympy.symbols('U x_1 x_2 p_1 p_2 m')
X, Xd, Xs, P, gi, gk, C = sympy.symbols('X Xd X^s P gi gk, C')
##########################################################################################
############################################################################################
# Konsumentteori 
## Opplysninger
U = 10*x_1**0.75*x_2**0.25
U.subs([(x_1,1),(x_2,2)])
############################################################################################
##### Lagring ###
afterms = set(dir())
modvardict = list(afterms - beforems)
modvardict.remove('beforems')
modeql = dict()
modeqs = dict()
for teller in range(0,len(modvardict)):
     eqvar = modvardict[teller]
     modeql[eqvar] = latex(eval(modvardict[teller]))
     #modeqs[eqvar] = str(eval(modvardict[teller]).rhs)
#####################################################################################################################
