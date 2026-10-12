# Theta graphs with shortest path three

Anonymous · revised candidate v1.1 · 12 October 2026

The manuscript proves that theta(a,b,3) is e-positive for every integer a>=b>=3. Together with cited results for shortest paths one and two, this covers shortest path at most three. It does not settle the full theta-graph conjecture.

Read [paper.tex](paper.tex) and [AI_INDEX.md](AI_INDEX.md). The composition expansion and reversal/full-fibre framework are inherited from Chen–He–Wang. The c=3 proof classifies negative terms and controls complete weighted preimage groups. The repaired preimage lemma uses actual crossing-window indices; the new equality proof classifies zero nonempty groups with first part at least two.

## Checks

From the repository root with Python 3:

```sh
python3 code/verify_all.py 24
python3 code/lemma6_check.py 24
python3 code/verify_csf.py code
python3 code/review_regressions.py
python3 -O code/review_regressions.py
```

See [REPLAY_RECEIPT.md](REPLAY_RECEIPT.md) for measured coverage and the publication-stage boundary. A nonzero process exit signals failure; read counts and scope as well as status. Bounded computations test identities and the implementation; the unrestricted theorem rests on the written proof and cited expansion. No proof-assistant or external journal-review assurance is claimed.

Original prose/data are CC0; original code is MIT. Third-party sources and supplied review material retain their own terms. Publication, DOI activation, archive integrity and public readback are separate gates, not asserted by this README.
