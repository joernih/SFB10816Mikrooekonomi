#######################################################################################
import sympy
from sympy import solve, Eq, symbols, latex, simplify
###########################################################################################
x,N, C, F = sympy.symbols('x N C F')
beforems = set(dir())
###########################################################################################
# Arbeidskrav
pf1 = Eq(x,2*N**0.50)
wn1 = 5
pn1 = 20
#### Løsning
dopdf1 = solve(pf1,x)[0].diff(N)
dtpdf1 = dopdf1.diff(N)
Fn1 = Eq(F,pn1*solve(pf1,x)[0]-wn1*N)
fob1_n = Eq(solve(Fn1,F)[0].diff(N),0)
ns1 = solve(fob1_n,N)[0]
xs1 = pf1.subs(N,ns1)
Fnv1 = Fn1.subs([(N,ns1)])
#ns1
#xs1
###########################################################################################
# Prøveeksamen
## Info
pn2 = Eq(x,4*N**0.50)
fk2 = 50000
cf2 = Eq(C,fk2+x**2)
p2 = 600
### Løsning
docf2 = solve(cf2,C)[0].diff(x)
dtcf2 = docf2.diff(x)
Fn2 = Eq(F,p2*x-solve(cf2,C)[0])
fob2_x = Eq(solve(Fn2,F)[0].diff(x),0)
xs2 = solve(fob2_x,x)[0]
Fnv2 = Fn2.subs([(x,xs2)])
ns2 = solve(pn2.subs(x,xs2),N)
#ns2
#xs2
###########################################################################################
# Eksamen
pn3 = Eq(x,N**0.50)
fk3 = 0
vk3 = 2*x**2
cf3 = Eq(C,fk3+vk3)
p3 = 100
### Løsning
docf3 = solve(cf3,C)[0].diff(x)
dtcf3 = docf3.diff(x)
Fn3 = Eq(F,p3*x-solve(cf3,C)[0])
fob3_x = Eq(solve(Fn3,F)[0].diff(x),0)
fob3_x
xs3 = solve(fob3_x,x)[0]
Fnv3 = Fn3.subs([(x,xs3)])
ns3 = solve(pn3.subs(x,xs3),N)
xs3
ns3
###########################################################################################
##########################################################################################
############################################################################################
afterms = set(dir())
modvardict = list(afterms - beforems)
modvardict.remove('beforems')
modeql = dict()
modeqs = dict()
for teller in range(0,len(modvardict)):
     eqvar = modvardict[teller]
     modeql[eqvar] = latex(eval(modvardict[teller]))
####################################################################################################################
