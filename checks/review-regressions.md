# Review regression execution

Date: 12 October 2026. Internal publication check, not external review.

Commands from the repository root, using configured Python 3.13.5:

```sh
python3 code/review_regressions.py
python3 -O code/review_regressions.py
```

Both completed with exit status 0. Each checked 25 admissible (a,b) pairs through n=16, 1,373 nonempty groups with first part at least two, and 46 zero groups. For every group the enumerated actual negative-preimage set equals the corrected crossing-window set without duplicate counting; zero total holds if and only if the stated gap shape holds.

Exact fixtures passed in both modes:

- Palindromic-prefix counterexample: B=5, J=(5,2,5), negative source (2,5,5); reversing all three target parts returns J but its actual crossing index is 1, disproving the old unrestricted converse.
- Weighted collision at (a,b)=(4,3): target (5,2,2), sources (2,2,5) and (2,5,2), contributions 60−8−8=44.
- Zero group at (4,4): target (4,2,2,2), source (2,2,4,2), contributions 24−24=0.
- General-c warning: theta(4,2,2), I=(2,2,3) gives C_I=−2, despite every part being less than a=4.

Four deliberately false expectations (missing window source, collision sum 52, false equality predicate, and general-c coefficient zero) were each rejected with RuntimeError and subprocess exit status 1. The driver requires those nonzero exits; a surviving mutation returns zero and fails the parent test. No Python `assert` is used, and optimized execution produces the same counts and rejections.

This regression imports the supplied lib3 definitions. It is not an independent implementation of the composition expansion, does not prove the unrestricted theorem by enumeration, and does not replace the analytic equality proof or the larger main replays. It tests the stated review repairs and explicit failure boundaries.
