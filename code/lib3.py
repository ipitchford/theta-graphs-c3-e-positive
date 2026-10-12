# Self-contained definitions for theta_{ab3}, c=3. Import from this dir.
from functools import lru_cache
def comps(n):
    if n==0: yield (); return
    for k in range(1,n+1):
        for r in comps(n-k): yield (k,)+r
def pref(I):
    s=[0]
    for x in I: s.append(s[-1]+x)
    return s
def thp(I,x): return min(v for v in pref(I) if v>=x)-x
def thm(I,x): return x-max(v for v in pref(I) if v<=x)
def w(I):
    r=I[0]
    for x in I[1:]: r*=x-1
    return r
def e2(xs): return sum(xs[i]*xs[j] for i in range(len(xs)) for j in range(i+1,len(xs)))
def pst(I,B):
    z=len(I); p=s=q=t=None
    for P in range(1,z+1):
        S=B-sum(I[:P-1])
        if 1<=S<=I[P-1]: p,s=P,S
    ext=list(I)+[I[0]]
    for Q in range(1,z+1):
        T=B-sum(I[1:Q])
        if 1<=T<=ext[Q]: q,t=Q,T
    return p,s,q,t
def Delta(I,B):
    p,s,q,t=pst(I,B)
    if I[0]<=I[p-1]-s: return s*(I[p-1]-s-I[0])
    return e2([I[p-1]-s]+list(I[p:q])+[t])
def phi(I,a):
    z=len(I)
    for k in range(z-1,-1,-1):
        if sum(I[k:])>=a: break
    if k==0: return I
    P,Q=I[:k],I[k:]; return (P[0],)+tuple(reversed(P[1:]))+Q
def D_thm32(I,a,b,c=3):
    """CHW Thm 3.2 coefficient, literal (phi form)."""
    B=b+c-1; R=tuple(reversed(phi(I,a)))
    return sum(thp(I,k) for k in range(2,c+1))-sum(thm(R,k) for k in range(a,a+c-1))+Delta(I,B)
def D3(I,a,b):
    """Reduced form (Lemma 1): Theta+(2)+Theta+(3)-Theta+(B-1)-Theta+(B)+Delta(B), B=b+2."""
    B=b+2
    return thp(I,2)+thp(I,3)-thp(I,B-1)-thp(I,B)+Delta(I,B)
def psi(I,B):
    p=pst(I,B)[0]; return tuple(reversed(I[:p]))+I[p:]
def psi3(I,B):
    if I[0]==1: return (1,)+psi(I[1:],B-1)
    return psi(I,B)
def pairs(N,nmin=8):
    for n in range(nmin,N+1):
        for b in range(3,n):
            a=n-b-2
            if a>=b: yield a,b
