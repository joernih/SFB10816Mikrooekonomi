##########################################################################################
#reticulate::repl_python()
##########################################################################################
import sympy
from sympy import *
###########################################################################################
# Oppgave 2: Konsumentteori (30 prosent)
# create a "symbol" called x
## Konsumentteori
#### Define function
U, x_1, x_2, p_1, p_2, m= sympy.symbols('U x_1 x_2 p_1 p_2 m')
p0_1 = 4
p0_2 = 5
m = 2000
U = x_1**0.5*x_2**0.5
S1 = sympy.Eq(U.diff(x_1)/U.diff(x_2),p0_1/p0_2)
S2 = sympy.Eq(m, p0_1*x_1+p0_2*x_2)
s0x_1 = solve(S2.subs(x_2,sympy.solve(S1,x_2)[0]),x_1)[0]
s0x_2 = solve(S2.subs(x_1,s0x_1),x_2)[0]
s0x_2
s0x_1
#
p1_1 = 2
p1_2 = 5
m = 2000
U = x_1**0.5*x_2**0.5
S1 = sympy.Eq(U.diff(x_1)/U.diff(x_2),p1_1/p1_2)
S2 = sympy.Eq(m, p1_1*x_1+p1_2*x_2)
s1x_1 = solve(S2.subs(x_2,sympy.solve(S1,x_2)[0]),x_1)[0]
s1x_2 = solve(S2.subs(x_1,s1x_1),x_2)[0]
s1x_2
s1x_1


## Elastisiteten
pdx = (s1x_1-s0x_1)/(s0x_1)
pdp = (p1_1-p0_1)/(p0_1)
pdx/pdp
###########################################################################################
# Oppgave 3: Markedsteori fullkomme (30 prosent)konkurranse
### Fullkommen konkurranse
## Produsentteori
x, xd, xs, p = sympy.symbols('x xd xs p')
XD =Eq(xd,600-6*p)
XS =Eq(xs,2*p)
## *** Solving the model
EQ = Eq(solve(XD,p)[0],solve(XS,p)[0]).subs(xs,x).subs(xd,x)
xeq = solve(EQ,x)[0]
peq = solve(XD.subs(xd,xeq),p)[0]

### Monopol
gi, gk = sympy.symbols('gi gk')
GK = solve(XS,p)[0].subs(xs,x)
I = solve(XD,p)[0].subs(xd,x)*x
GI = I.diff(x)
GIGK = Eq(GI,GK)

# Kvantum
xmeq = solve(GIGK,x)[0]
# Pris
pmeq = solve(XD,p)[0].subs(xd,xmeq)
pimeq = GI.subs(x,xmeq)

# ((pmeq-pimeq)*(xeq-xmeq))/2

((pmeq-pimeq)*(xeq-xmeq))/2
###########################################################################################
# Oppgave 3: Markedsteori fullkomme (30 prosent)konkurranse
### Fullkommen konkurranse
## Produsentteori
x, xd, xs, p = sympy.symbols('x xd xs p')
XD =Eq(xd,800-4*p)
XS =Eq(xs,-40+2*p)
## *** Solving the model
EQ = Eq(solve(XD,p)[0],solve(XS,p)[0]).subs(xs,x).subs(xd,x)
xeq = solve(EQ,x)[0]
peq = solve(XD.subs(xd,xeq),p)[0]
xeq
peq

