# Composition-method helpers: w_I, Theta^+, Delta_I(b) (Wang, cycle-chords), coeffs_iter = verified e_I-expansion of theta graphs.
# Chen-He-Wang Theorem 3.2 machinery: Theta+/-, Delta_I(b), phi, d'_I ; test pointwise nonnegativity.
import itertools, sys
from collections import defaultdict
from fractions import Fraction
def compositions(n):
    for k in range(1,n+1):
        for cuts in itertools.combinations(range(1,n),k-1):
            pts=(0,)+cuts+(n,); yield tuple(pts[i+1]-pts[i] for i in range(k))
def w(I):
    r=I[0]
    for x in I[1:]: r*=x-1
    return r
def psums(I):
    s=[0]
    for x in I: s.append(s[-1]+x)
    return s
def thp(I,a): return min(v for v in psums(I) if v>=a)-a
def e2(xs): return sum(xs[i]*xs[j] for i in range(len(xs)) for j in range(i+1,len(xs)))
def Delta(I,b):
    z=len(I); P=psums(I)
    # b = i1+..+i_{p-1}+s, 1<=s<=ip
    p=next(k for k in range(1,z+1) if P[k-1]<b<=P[k]); s=b-P[p-1]
    # b = i2+..+iq + t, 1<=t<=i_{q+1}, convention i_{z+1}=i1 ; q in 1..z
    Q=[0]
    for x in I[1:]+(I[0],): Q.append(Q[-1]+x)   # Q[k]= i2+..+i_{k+1}
    q=next(k for k in range(1,z+1) if Q[k-1]<b<=Q[k]); t=b-Q[q-1]
    ip=I[p-1]
    if I[0]<=ip-s: return s*(ip-s-I[0])
    return e2([ip-s]+list(I[p:q])+[t])

def to_e(coef):
    X=defaultdict(int)
    for I,v in coef.items(): X[tuple(sorted(I,reverse=True))]+=v*w(I)
    return {k:v for k,v in X.items() if v}
def classes(coef):
    C=defaultdict(int)
    for I,v in coef.items(): C[(I[0],tuple(sorted(I[1:])))]+=v
    return C
def coeffs_iter(a,b,c, variant=0):
    # X = CC(n-b,b) + sum_{k=1}^{c-1} [ tadpole(cycle a+b+k-1, tail c-k) - tadpole(cycle a+k-1, tail b+c-k) ]
    n=a+b+c-1; out={}
    for I in compositions(n):
        if w(I)==0: continue
        v=Delta(I,b)
        for k in range(1,c):
            v+=thp(I,c-k+1)-thp(I,a+k)
        out[I]=v
    return out

if __name__=="__main__":
    from csf import csf_e, theta
    failures = 0
    for a,b,c in [(3,2,1),(3,3,2),(4,3,2),(4,3,3),(5,4,3),(5,5,4),(6,4,4)]:
        co=coeffs_iter(a,b,c)
        direct={k:int(v) for k,v in csf_e(*theta(a,b,c)).items() if v}
        agrees=to_e(co)==direct
        print((a,b,c), "formula==direct:", agrees)
        failures += not agrees
    sys.exit(1 if failures else 0)
