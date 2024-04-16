########################################################################################
import sympy
from sympy import *
###########################################################################################
x, N, K, w, r, C, P, F=sympy.symbols('X N K w r C P F')
U, x_1, x_2, p_1, p_2, m= sympy.symbols('U x_1 x_2 p_1 p_2 m')
X, Xd, Xs, p, gi, gk = sympy.symbols('X Xd Xs P gi gk')
###########################################################################################
# Oppgave 1: Produsentteori 
## Info
### a
pfe = 2*N**0.2*K**0.2
wn = 100
rn = 25
xn = 16
pf = sympy.Eq(x,pfe)
isc = sympy.Eq(C,N*w+K*r)
cf = sympy.Eq(C,20*x**2)
### b
Fx = sympy.Eq(F, p*x-solve(cf,C)[0])
pcx = 1000
## Calculations
### a
pfdn=simplify(diff(solve(pf,x)[0],N))
pfdk=simplify(diff(solve(pf,x)[0],K))
pfdn2=simplify(diff(pfdn,N))
pfdk2=simplify(diff(pfdk,K))
sympy.N(solve(pf,x)[0].subs([(N,10),(K,10)]))
sympy.N(solve(pf,x)[0].subs([(N,20),(K,20)]))
MTSB = simplify(pfdn/pfdk)
foc = Eq(MTSB,w/r)
ns=solve(foc.subs([(w,wn),(r,rn)]),N)[0]
kstar=solve(pf.subs([(x,xn),(N,ns)]),K)[0]
nstar=ns.subs(K,kstar)
solve(pf.subs([(K,kstar),(N,nstar)]),x)[0]
### b
diff(solve(cf,C)[0],x)
dFX=diff(solve(Fx,F)[0],x)
xopt=solve(dFX,x)[0].subs(p,pcx)
dFX2=diff(dFX,x)
solve(Fx,F)[0].subs(([x,xopt],[p,pcx]))
###########################################################################################
# Oppgave 2: Konsumentteori 
p0_1 = 50
p0_2 = 100
m = 1000
U = x_1**0.25*x_2**0.5
S1 = sympy.Eq(U.diff(x_1)/U.diff(x_2),p0_1/p0_2)
S2 = sympy.Eq(m, p0_1*x_1+p0_2*x_2)
s0x_1 = solve(S2.subs(x_2,sympy.solve(S1,x_2)[0]),x_1)[0]
s0x_2 = solve(S2.subs(x_1,s0x_1),x_2)[0]
###########################################################################################
avg = 6
XD = Eq(P,24-2*X)
XS = Eq(P,4*X)
XSa = Eq(P,solve(XS,P)[0]+avg)
XDt = solve(XD,P)[0].subs(X,0)
XSt = solve(XS,P)[0].subs(X,0)
XSa = solve(XS,P)[0].subs(X,0)
XSa
XSta = solve(XSa,P)[0]


.subs(X,0)
MBV = Eq(solve(XD,P)[0],solve(XS,P)[0])
X_fk = solve(MBV,X)
p_fk = solve(XD.subs(X,X_fk[0]),P)
ko=(X_fk[0]-0)*(XDt-p_fk[0])/2
XDt
p_fk[0]
X_fk[0]
po=(p_fk[0]-XSt)*(X_fk[0]-0)/2
so=ko+po
so
XSta =solve(XSa.subs(x,0),P)
MBVa = Eq(solve(XD,P)[0],solve(XSa,P)[0])
X_fka = solve(MBVa,X)
p_fka = solve(XD.subs(X,X_fka[0]),P)
p_dka = solve(XS.subs(X,X_fka[0]),P)
koa=(X_fka[0]-0)*(XDt-p_fka[0])/2
poa=(X_fka[0]-0)*(p_dka[0]-0)/2
dvt=(X_fk[0]-X_fka[0])*(p_fka[0]-p_dka[0])/2
sia=(X_fka[0]-0)*(p_fka[0]-p_dka[0])
X_fk
dvt
## a)
X_fk[0]
p_fk[0]
## b)
MBVa
ko
po
so
## c)
p_fka[0]
p_dka[0]
X_fk[0]
X_fka[0]
## d)
sympy.N(koa)
sympy.N(poa)
sympy.N(sia)
## e)
sympy.N(dvt)

