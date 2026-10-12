# Exact chromatic symmetric function in e-basis: X_G = sum_{S subset E} (-1)^|S| p_{type(S)}, p -> e via Newton.
from fractions import Fraction
from math import factorial
from functools import lru_cache
from collections import Counter, defaultdict
def partitions(n, m=None):
    if m is None: m=n
    if n==0: yield (); return
    for k in range(min(n,m),0,-1):
        for r in partitions(n-k,k): yield (k,)+r
@lru_cache(None)
def p_in_e(k):  # p_k = sum_{lam |- k} (-1)^{k-l} k (l-1)!/prod m_i! e_lam
    out={}
    for lam in partitions(k):
        l=len(lam); c=Counter(lam); den=1
        for v in c.values(): den*=factorial(v)
        out[lam]=Fraction((-1)**(k-l)*k*factorial(l-1),den)
    return out
def mul(A,B):
    out=defaultdict(Fraction)
    for a,x in A.items():
        for b,y in B.items(): out[tuple(sorted(a+b,reverse=True))]+=x*y
    return out
@lru_cache(None)
def p_lam_in_e(lam):
    r={():Fraction(1)}
    for k in lam: r=mul(r,p_in_e(k))
    return dict(r)
def csf_p(nv, edges):
    # sum over edge subsets via DP on components: iterate subsets explicitly (edges <= ~20)
    out=defaultdict(int); m=len(edges)
    for mask in range(1<<m):
        par=list(range(nv))
        def f(x):
            while par[x]!=x: par[x]=par[par[x]]; x=par[x]
            return x
        cnt=0
        for i in range(m):
            if mask>>i&1:
                cnt+=1; a,b=f(edges[i][0]),f(edges[i][1])
                if a!=b: par[a]=b
        sz=Counter(f(v) for v in range(nv)); lam=tuple(sorted(sz.values(),reverse=True))
        out[lam]+=(-1)**cnt
    return out
def csf_e(nv,edges):
    res=defaultdict(Fraction)
    for lam,c in csf_p(nv,edges).items():
        if c:
            for mu,x in p_lam_in_e(lam).items(): res[mu]+=c*x
    return {k:v for k,v in res.items() if v}
def theta(a,b,c):
    # endpoints 0,1; paths of lengths a,b,c
    edges=[]; nv=2
    for L in (a,b,c):
        prev=0
        for i in range(L-1): edges.append((prev,nv)); prev=nv; nv+=1
        edges.append((prev,1))
    return nv,edges
