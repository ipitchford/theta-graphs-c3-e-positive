# Exact check of the Lemma 6 proof (theta-c3-theorem-v2.md, Section 4, Lemma 6) for all a>=b>=3, n<=N.
# For every target J (J_1=m>=2) of an i_1>=2 group it checks, with exact rationals:
#  (P1) the predicted preimage set {H_j : j in pred} equals the actual set psi^{-1}(J) ∩ N;
#  (P2) D_J = A + sum_i g_i S_i  (gap decomposition);
#  (P3) per-preimage bound: N1/N3 at gap i has cost <= g_i S_i + delta_i, delta_i>0 only at one index,
#       delta_i <= 4-8/m (y=2,S=2), 3-9/m (y=3,S=2), 2-8/m (y=2,S=3); N2 cost <= its stated bound;
#  (P4) A - cost_N2 - delta >= 0 ; (P5) c_J >= 0, D_J > 0 ; tight cases are exactly m=4,r=0,L=1,g=(0,2,2),J_k=2.
import sys,os; sys.path.insert(0,os.path.dirname(os.path.abspath(__file__))); from lib3 import *
from collections import defaultdict, Counter
from fractions import Fraction as Fr
N=int(sys.argv[1]); fails=Counter(); pats=Counter(); tight=Counter(); ng=0
for a,b in pairs(N):
    B=b+2; n=a+b+2; Dd={I:D3(I,a,b) for I in comps(n) if w(I)}
    pre=defaultdict(list)
    for I,d in Dd.items():
        if d<0 and I[0]>=2: pre[psi(I,B)].append(I)
    for J,L in pre.items():
        ng+=1; m=J[0]; P=pref(J); z=len(J)
        k=next(i for i in range(1,z+1) if P[i-1]<B<=P[i]); sJ=B-P[k-1]; r=P[k]-B
        if r>=m: fails['branch1 target with preimage']+=1; continue
        q=max(i for i in range(k,z+1) if P[i]<B+m); t=B+m-P[q]
        g=[J[k+i-1] for i in range(1,q-k+1)]; Lg=len(g)
        U=r if sJ==1 else 2*r+1
        A=2*m-5-U+r*(m-r) if m>=3 else None
        S=[sum(g[i:])+t for i in range(Lg+1)]   # S[i] = g_{i+1}+...+g_L+t (S[0]=m-r)
        if m>=3 and Dd[J]!=A+sum(g[i-1]*S[i] for i in range(1,Lg+1)): fails['P2']+=1
        def H(j): return tuple(reversed(J[:j]))+J[j:]
        pred={}
        if k>=2 and sJ==1 and S[0]>=2: pred[k]='N2'
        for i in range(1,Lg+1): pred[k+i]='N1' if (i==Lg and t==1) else 'N3'
        actual={j:None for j in range(2,z+1) if H(j) in L}
        predN={j:ty for j,ty in pred.items() if Dd.get(H(j),0)<0}
        if set(actual)!=set(predN) or len(actual)!=len(L): fails['P1']+=1; continue
        rho=lambda y:Fr(y*(m-1),m*(y-1))
        costN2=Fr(0); delta=Fr(0); ndef=0; key=[]
        for j,ty in sorted(predN.items()):
            Hj=H(j); y=J[j-1]; c=rho(y)*(-Dd[Hj]); key.append((ty,j-k))
            if w(Hj)*m*(y-1)!=w(J)*y*(m-1): fails['weight ratio']+=1
            if ty=='N2':
                costN2=c
                if c>Fr(3*(m-1),m): fails['N2 bound']+=1
            else:
                i=j-k; gain=y*S[i]; d=c-gain
                if d>0:
                    ndef+=1; delta+=d
                    bd={(2,2):4-Fr(8,m),(3,2):3-Fr(9,m),(2,3):2-Fr(8,m)}.get((y,S[i]))
                    if bd is None or d>bd: fails['P3 deficit']+=1
        if ndef>1: fails['P3 >1 deficit']+=1
        if A is None or A-costN2-delta<0: fails['P4']+=1
        cJ=Dd[J]*w(J)+sum(Dd[h]*w(h) for h in L)
        if cJ<0 or Dd[J]<=0: fails['P5']+=1
        if cJ==0:
            tight[(m,r,Lg,tuple([r]+g+[t]),J[k-1])]+=1
            if not (m==4 and r==0 and Lg==1 and g==[2] and t==2 and J[k-1]==2): fails['unexpected tight']+=1
        pats[(k==1,sJ==1,tuple(key))]+=1
print("N<=",N,"groups",ng); print("patterns",len(pats))
for kk,v in sorted(pats.items()): print(" ",kk,v)
print("tight",dict(tight)); print("FAILURES:",dict(fails) if fails else "none")
sys.exit(1 if fails else 0)
