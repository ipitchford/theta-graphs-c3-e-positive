# Exact verification of Lemmas 1-6 of theta-c3-theorem.md for all a>=b>=3, n=a+b+2<=N.
import sys,os; sys.path.insert(0,os.path.dirname(os.path.abspath(__file__))); from lib3 import *
from collections import defaultdict
N=int(sys.argv[1]); fails=defaultdict(int); cnt=defaultdict(int)
def Tlow(I):
    x=I[0]
    return 2*I[1]-3 if x==1 else (I[1]-1 if x==2 else 2*x-5)
def Dclosed(I,B):   # Lemma 2
    x=I[0]; p,s,q,t=pst(I,B); ip=I[p-1]; r=ip-s
    if p==1: return 2*B-6+Delta(I,B)
    if r>=x:
        return Tlow(I)-x if s==1 else Tlow(I)-2*x-1+(s-2)*(r-x)
    return Tlow(I)-(2*r+1 if s>=2 else r)+e2([r]+list(I[p:q])+[t])
def Npred(I,B):     # Lemma 3: returns predicted D if I in N else None
    x=I[0]; p,s,q,t=pst(I,B); r=I[p-1]-s
    if p==1: return None
    T=Tlow(I)
    if (s==1 and r>=x) or (s>=2 and r==x-1):
        v=T-x; return v if v<0 else None
    if s>=2 and r>=x:
        v=T-2*x-1+(s-2)*(r-x); return v if v<0 else None
    return None
for a,b in pairs(N):
    B=b+2; n=a+b+2; Dd={}
    for I in comps(n):
        if not w(I): continue
        d=D3(I,a,b); Dd[I]=d; cnt['comp']+=1
        if D_thm32(I,a,b)!=d: fails['L1 reduction']+=1
        if Dclosed(I,B)!=d: fails['L2 closed form']+=1
        pv=Npred(I,B)
        if (d<0)!=(pv is not None) or (pv is not None and pv!=d): fails['L3 N-characterisation']+=1
        if d<0 and d<-6: fails['L3 D>=-6']+=1
    pre=defaultdict(list)
    for I,d in Dd.items():
        if d<0: pre[psi3(I,B)].append(I)
    for J,L in pre.items():
        cnt['groups']+=1
        if w(J)==0: fails['target w=0']+=1; continue
        if Dd[J]<0: fails['target in N']+=1
        tot=Dd[J]*w(J)+sum(Dd[H]*w(H) for H in L)
        if tot<0: fails['group sum<0 (A)' if J[0]>=2 else 'group sum<0 (B)']+=1
        if J[0]==1:
            cnt['B groups']+=1
            if len(L)>2: fails['B: >2 preimages']+=1
            if any(w(H)!=w(J) for H in L): fails['B: weights differ']+=1
            if any(H[1]!=2 for H in L): fails['B: k1!=2']+=1
            if Dd[J]+sum(Dd[H] for H in L)<0: fails['B: unit inequality']+=1
        else: cnt['A groups']+=1
    # final: all regrouped coefficients nonnegative
    c=defaultdict(int)
    for I,d in Dd.items():
        c[psi3(I,B) if d<0 else I]+=d*w(I)
    if min(c.values())<0: fails['final c_J<0']+=1
    cnt['pairs']+=1
print("N<=",N,dict(cnt)); print("FAILURES:",dict(fails) if fails else "none")
sys.exit(1 if fails else 0)
