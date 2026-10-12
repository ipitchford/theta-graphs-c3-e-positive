# Check X_theta(a,b,3) = sum_I D_I w_I e_I (Thm 3.2, c=3) against brute-force CSF; edges=a+b+3<=15.
import sys,os; sys.path.insert(0,os.path.dirname(os.path.abspath(__file__))); from lib3 import *
sys.path.insert(0,sys.argv[1]); from csf import csf_e, theta
from collections import defaultdict
from fractions import Fraction
failures = 0
for a,b in [(3,3),(4,3),(5,3),(4,4),(6,3),(5,4),(7,3),(6,4),(5,5)]:
    tot=defaultdict(int)
    for I in comps(a+b+2):
        if w(I): tot[tuple(sorted(I,reverse=True))]+=D3(I,a,b)*w(I)
    tr={k:v for k,v in csf_e(*theta(a,b,3)).items() if v}
    agrees = {k:Fraction(v) for k,v in tot.items() if v}==tr
    print((a,b,3), agrees)
    failures += not agrees
sys.exit(1 if failures else 0)
