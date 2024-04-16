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
x_1 = sympy.symbols('x_1')
x_2 = sympy.symbols('x_2')
U = 10*x_1**0.75*x_2**0.25
p0_1 =60 # 90
p0_2 =10 # 30
m0 = 600
## Utregninger
Un=Eq(U_a,U)
alt_1=m0/p0_1
alt_2=m0/p0_2
heln=p0_1/p0_2
msb = U.diff(x_1)/U.diff(x_2)
S1 = sympy.Eq(msb,p0_1/p0_2)
S2 = sympy.Eq(m0,p0_1*x_1+p0_2*x_2)
sympy.solve(S1,x_1)[0]
sympy.solve(S1,x_2)[0]
s0x_1 = sympy.solve(S2.subs(x_2,sympy.solve(S1,x_2)[0]),x_1)[0]
s0x_2 = sympy.solve(S2.subs(x_1,s0x_1),x_2)[0].subs(m,m0)
Ul = round(U.subs([(x_1,s0x_1),(x_2,s0x_2)]),2)
## Utregninger
### a
alt_1
alt_2
heln
### b
s0x_1
s0x_2
### c
### d
Ul
### Kontroll
p0_1*s0x_1+p0_2*s0x_2
###########################################################################################
## Markedsteori 
### Monopol
##########################################################################################
## Opplysninger
### Tilbudssiden
CX = Eq(C,100000+3000*X)
CXs = solve(CX,C)[0]
#CX = Eq(C,100000+3000*X)
#### Etterspørselssiden
MBV = Eq(P,5000-4*X)
#MBV = Eq(P,5000-2*X)
## Utregninger
### Samfunnsøkonomis optimal tilpasning
cx = solve(CX,C)[0].diff(X)
bet = Eq(solve(MBV,P)[0],cx)
xeq = solve(bet,X)[0]
peq = solve(MBV.subs(X,xeq),P)[0]
## Monopol
MBV0 = solve(MBV.subs(X,0))[0]
I = solve(MBV,P)[0]*X
GI = I.diff(X)
GIGK = Eq(GI,cx)
xmeq = solve(GIGK,X)[0]
pmeq = solve(MBV.subs(X,xmeq),P)[0]
### KO
ko = (xmeq)*(MBV0-pmeq)/2
### PO
po = (xmeq)*(pmeq-cx)
### DT
dtap = (xeq-xmeq)*(pmeq-cx)/2
### a
cx
### b  
xmeq
pmeq
### c
ko
po
dtap
peq
xeq
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
