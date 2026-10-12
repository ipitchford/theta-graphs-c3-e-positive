# Independent recheck (coordinator implementation, separate from lib3.py):
# (1) D_I (Lemma 1 form) summed against brute-force CSF; (2) psi_3 regrouping gives c_J>=0 and no target in N.
import sys,os; sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from comp import compositions, w, thp, Delta, to_e
from csf import csf_e, theta
from collections import defaultdict
def D(I,a,b):
    B=b+2; return thp(I,2)+thp(I,3)-thp(I,B-1)-thp(I,B)+Delta(I,B)
def psi(I,B):
    P=0
    for p,x in enumerate(I):
        P+=x
        if P>=B: break
    return tuple(reversed(I[:p+1]))+I[p+1:]
def psi3(I,B): return (1,)+psi(I[1:],B-1) if I[0]==1 else psi(I,B)
AMAX=int(sys.argv[1]); CSFMAX=int(sys.argv[2])
fails=0; checked=0; csfchecked=0
for a in range(3,AMAX+1):
  for b in range(3,a+1):
    n=a+b+2; B=b+2; co={I:D(I,a,b) for I in compositions(n) if w(I)}
    if a+b<=CSFMAX:
        if to_e(co)!={k:int(v) for k,v in csf_e(*theta(a,b,3)).items()}: fails+=1; print("CSF mismatch",a,b)
        csfchecked+=1
    c=defaultdict(int); N={I for I,v in co.items() if v<0}
    for I,v in co.items(): c[psi3(I,B) if I in N else I]+=v*w(I)
    for J,v in c.items():
        if v<0: fails+=1; print("negative",a,b,J,v)
        if J in N: fails+=1; print("target in N",a,b,J)
    checked+=1
print(f"pairs {checked}; csf-compared {csfchecked}; FAILURES: {fails}")
sys.exit(1 if fails else 0)
