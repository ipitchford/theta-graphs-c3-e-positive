"""Exact internal review regressions; shared lib3 is a stated dependency."""
import argparse
from collections import defaultdict
import json
from pathlib import Path
import subprocess
import sys
from lib3 import comps, pairs, pref, pst, w, D3, Delta, thp, psi

def require(condition, message):
    if not condition:
        raise RuntimeError(message)

def window_sources(J, B, a, b):
    P=pref(J); m=J[0]
    result=[]
    for j in range(2,len(J)+1):
        H=tuple(reversed(J[:j]))+J[j:]
        window=B<=P[j]<=B+m-1
        require((pst(H,B)[0]==j)==window,'crossing-window equivalence')
        if window:
            require(psi(H,B)==J,'window reversal')
            if D3(H,a,b)<0: result.append(H)
    require(len(result)==len(set(result)),'duplicate negative preimage')
    return set(result)

def shape(J,B):
    P=pref(J);m=J[0];k=pst(J,B)[0];r=P[k]-B
    if r>=m: return False
    q=max(i for i in range(k,len(J)+1) if P[i]<B+m)
    g=tuple(J[k:q]);t=B+m-P[q]
    return m==4 and r==0 and q-k==1 and g==(2,) and t==2 and J[k-1]==2

def general_c(I,a,b,c):
    return Delta(I,b)+sum(thp(I,k) for k in range(2,c+1))-sum(thp(I,k) for k in range(a+1,a+c))

def fixtures(mutation=None):
    J=(5,2,5);H=(2,5,5); B=5
    require(D3(H,7,3)==-1 and psi(H,B)==J,'palindromic negative source')
    H3=tuple(reversed(J))
    require(psi(H3,B)==J and pst(H3,B)[0]==1 and sum(J)>B+J[0]-1,'false-converse counterexample')
    sources=window_sources(J,B,7,3)
    require(sources==({H} if mutation!='window' else set()),'negative-window bijection')
    J=(5,2,2); hs=[(2,2,5),(2,5,2)]
    pieces=[D3(J,4,3)*w(J)]+[D3(h,4,3)*w(h) for h in hs]
    require(all(psi(h,5)==J for h in hs),'collision destinations')
    require(pieces==[60,-8,-8] and sum(pieces)==(44 if mutation!='collision' else 52),'weighted full collision')
    J=(4,2,2,2);H=(2,2,4,2)
    require(D3(J,4,4)*w(J)==24 and D3(H,4,4)*w(H)==-24 and psi(H,6)==J,'zero group')
    require(shape(J,6)==(mutation!='equality'),'zero equality predicate')
    require(general_c((2,2,3),4,2,2)==(-2 if mutation!='general-c' else 0),'general-c negative counterexample')
    return {'palindromic_counterexample':True,'collision':[60,-8,-8,44],'zero_group':[24,-24,0],'general_c':-2}

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--max-n',type=int,default=16)
    parser.add_argument('--mutation',choices=['window','collision','equality','general-c'])
    args=parser.parse_args()
    result=fixtures(args.mutation)
    if args.mutation: return
    require(8<=args.max_n<=16,'bounded check requires 8<=max-n<=16')
    ng=nzero=graphs=0
    for a,b in pairs(args.max_n):
        graphs+=1;B=b+2;n=a+b+2;groups=defaultdict(list)
        for I in comps(n):
            if I[0]>=2 and w(I) and D3(I,a,b)<0:
                groups[psi(I,B)].append(I)
        for J,actual in groups.items():
            ng+=1
            require(window_sources(J,B,a,b)==set(actual),'exhaustive negative-window mismatch')
            total=D3(J,a,b)*w(J)+sum(D3(H,a,b)*w(H) for H in actual)
            require(total>=0,'negative weighted group')
            require((total==0)==shape(J,B),'equality iff mismatch')
            nzero+=total==0
    controls={}
    for mutation in ['window','collision','equality','general-c']:
        command=[sys.executable]+(['-O'] if sys.flags.optimize else [])+[str(Path(__file__).resolve()),'--mutation',mutation]
        child=subprocess.run(command,capture_output=True,text=True)
        require(child.returncode!=0 and 'RuntimeError:' in child.stderr,'negative control accepted: '+mutation)
        controls[mutation]=child.returncode
    result.update(status='pass',max_n=args.max_n,graphs=graphs,groups=ng,zero_groups=nzero,negative_controls=controls,optimized=bool(sys.flags.optimize),scope='Internal regression using supplied lib3; not independent verification of literature expansion')
    print(json.dumps(result,indent=2))

if __name__=='__main__': main()
