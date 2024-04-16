########################################################################################
import sympy
from sympy import *
###########################################################################################
x, N, K, w, r, C, P, F, Co=sympy.symbols('x N K w r C P F C_o')
U, x_1, x_2, p_1, p_2, m= sympy.symbols('U x_1 x_2 p_1 p_2 m')
X, Xd, Xs, p, gi, gk = sympy.symbols('X Xd Xs P gi gk')
beforems = set(dir())
###########################################################################################
# Oppgave 2: Produsentteori 
## Info
### a
pfe = 4*N**0.75*K**0.25
wn = 30
rn = 10
xn = 100
pf = sympy.Eq(x,pfe)
isc = sympy.Eq(Co,N*w+K*r)
#### a
pfdn=simplify(diff(solve(pf,x)[0],N))
pfdk=simplify(diff(solve(pf,x)[0],K))
# b
MTSB = simplify(pfdn/pfdk)
MTSBn = MTSB.subs([(K,4),(N,4)])
# c
iscn = isc.subs([(w,wn),(r,rn)])
# d
foc = Eq(MTSB,w/r).subs([(w,wn),(r,rn)])
ns=solve(foc.subs([(w,wn),(r,rn)]),N)[0]
kstar=solve(pf.subs([(x,xn),(N,ns)]),K)[0]
nstar=ns.subs(K,kstar)
nstar
kstar
solve(pf.subs([(K,kstar),(N,nstar)]),x)[0]
#############################################################################################
############################################################################################
## Oppgave 3 Markdsteori
#avg = 6
#XD = Eq(P,24-2*X)
#XS = Eq(P,4*X)
#XSa = Eq(P,solve(XS,P)[0]+avg)
#XDt = solve(XD,P)[0].subs(X,0)
#XSt = solve(XS,P)[0].subs(X,0)
#XSta = solve(XSa,P)[0].subs(X,0)
#MBV = Eq(solve(XD,P)[0],solve(XS,P)[0])
#X_fk = solve(MBV,X)
#p_fk = solve(XD.subs(X,X_fk[0]),P)
#ko=(XDt-p_fk[0])*(X_fk[0]-0)/2
#po=(p_fk[0]-XSt)*(X_fk[0]-0)/2
#so=ko+po
#XSta =solve(XSa.subs(x,0),P)
#MBVa = Eq(solve(XD,P)[0],solve(XSa,P)[0])
#X_fka = solve(MBVa,X)
#p_fka = solve(XD.subs(X,X_fka[0]),P)
#p_dka = solve(XS.subs(X,X_fka[0]),P)
#koa=(X_fka[0]-0)*(XDt-p_fka[0])/2
#poa=(X_fka[0]-0)*(p_fka[0]-XSta[0])/2
#dvt=(X_fk[0]-X_fka[0])*(p_fka[0]-p_dka[0])/2
#sia=(X_fka[0]-0)*(p_fka[0]-p_dka[0])
### a)
#X_fk[0]
#p_fk[0]
### b)
#MBVa
#ko
#po
#so
### c)
#p_fka[0]
#p_dka[0]
#X_fk[0]
#X_fka[0]
### e)
#sympy.N(dvt)
#
############################################################################################
##### lagring ###
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
