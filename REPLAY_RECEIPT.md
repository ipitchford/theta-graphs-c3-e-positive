# Exact-check receipt

Date: 12 October 2026. Revised working-tree checks; final archive extraction and publication readback are not certified here.

The publication coordinator confirmed the following completed main runs, each exit status 0:

| Command | Actual coverage/result |
|---|---|
| `python3 code/verify_all.py 24` | 971,165 compositions, 170,224 groups, 81 graph parameter pairs |
| `python3 code/lemma6_check.py 24` | 124,325 groups, 65 patterns, 3,926 zero groups; no reported failures |
| `python3 code/verify_csf.py code` | Nine small graph comparisons, all True |

The targeted regression agent executed `python3 code/review_regressions.py` and `python3 -O code/review_regressions.py` using Python 3.13.5. Both exited 0: 25 graphs, 1,373 groups, 46 zero groups through n=16. Each mode rejected four semantic mutations with exit status 1. Exact fixture values were 60−8−8=44, 24−24=0 and the general-c coefficient −2. Details: checks/review-regressions.md.

These are exact integer/rational checks, not statistical evidence. They are internal coordinated verification. The regression shares lib3 and is not an independent implementation of the literature identity. Finite coverage does not replace the unrestricted proof. Final frozen-byte hashes, clean-extraction gates and public asset verification must be recorded separately before publication closeout.
