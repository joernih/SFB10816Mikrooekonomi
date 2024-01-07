####################################################################################################################
########################################################################################################################
# Cleaning namespace
for name in dir():
  if not name.startswith('_'):
      del globals()[name]
# Import packages
#import json
import sympy
import numpy
import sys
from sympy import solve, Eq, symbols, latex, simplify, diff
import pandas
import os
import rpy2
import rpy2.robjects as robjects
from rpy2.robjects.packages import importr, data
rroot=importr('rprojroot')
abs_path = rroot.find_rstudio_root_file()[0]
csvfile=abs_path+'/seminar/oppgaver/abc.csv'
readmodvar = pandas.read_csv(csvfile, sep=',') 
sympy.var(readmodvar.iloc[:,0])
beforems = set(dir())
#####  ###
########################################################################################################################
#########################################################################################################################
##### Oppgave 1
op1a=[Eq(u,x**2*x**3)]
op1b=[Eq(u,x*x**4)]
op1c=[Eq(u,y+y)]
op1d=[Eq(u,y**2+y)]
op1e=[Eq(u,(x1+x2)*x**0.5)]
op1f=[Eq(u,x1**3/x1)]
op1g=[Eq(u,x1**3/x2)]
###### Oppgave 2
op2a=[Eq(y**2, a*b)]
op2b=[Eq(x**0.5, a*b)]
###### Oppgave 3
op3a=[Eq(f,4*x**3)]
op3b=[Eq(f,4*x**5+2*x**-3)]
op3c=[Eq(f,1/6*x**6*a)]
op3d=[Eq(f,1/6*x**6*a+a)]
op3e=[Eq(f,5*x/2*x**2)]
op3f=[Eq(f,5*x**4+3*y**0.5)]
op3g=[Eq(f,1/2*x**0.5+x*y**0.5)]
op3h=[Eq(f,3*x**(1/6)*y**2+y**1/3**x**3)]
op3i=[Eq(f,3*x1**1/6*y**2+y**1/3**x**3)]
##### Oppgave 4
op4a=[Eq(u,1/3)]
op4b=[Eq(u,1/3)]
op4c=[Eq(u,1/3)]
op4e=[Eq(u,1/3)]
op4f=[Eq(u,1/3)]
op4g=[Eq(u,1/3)]
op4h=[Eq(u,1/3)]
##### Oppgave 5
op5a=[Eq(fxy,-4*x**2-2*x*y-3.5*y)]
op5b=[Eq(fxy,-2*x**2-2*x*y-3.5*y)]
##########################################################################################################################
###### Storing ###
##### Storing ###
afterms = set(dir())
modvarlist = list(afterms - beforems)
modvarlist.remove('beforems')
modvarlist
modeqs = dict()
modeql = dict()
dfs = [] 
dfl = [] 
parv = 'empty'
for i in range(0,len(modvarlist)):
  modeqs[parv] = dfs
  modeql[parv] = dfl
  parv = modvarlist[i]
  dfs = [] 
  dfl = [] 
  nid = len(eval(modvarlist[i])) 
  for j in range(0,nid):
    dfs.append(str(eval(modvarlist[i])[j].rhs))
    dfl.append(latex(eval(modvarlist[i])[j].rhs))
modeqs[parv] = dfs
modeql[parv] = dfl
modeqs.pop('empty')
modeql.pop('empty')
##########################################################################################################################
