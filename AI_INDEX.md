# AI index

## Statement and reading order

Read [README-v1.1.md](README-v1.1.md), [paper.tex](paper.tex), [CLAIMS.json](CLAIMS.json), then [ASSURANCE.md](ASSURANCE.md). The graph has three internally disjoint paths of edge lengths a,b,3 and a+b+2 vertices. Claim: e-positivity for all integers a>=b>=3. This is not the full theta conjecture.

## Dependencies and new work

[CITATION_AUDIT.md](CITATION_AUDIT.md) distinguishes Wang's c=1 theorem, Chen–He–Wang's c=2 theorem and composition expansion, and the c=3 negative-group accounting. [bibliography.bib](bibliography.bib) gives source identifiers. The inherited general-c expansion is not a contribution of this package.

## Proof navigation

In paper.tex, follow labels lem:pre, lem:one and lem:main. The corrected preimage window gives a bijection only for actual crossing indices. A target may have multiple negative sources: use all weighted contributions. The gap analysis permits at most one positive deficit. Zero groups with first part at least two have exactly the stated (0,2,2) gap shape with m=4 and crossing part two. Do not extrapolate this to partition-level zero coefficients.

## Executable checks

[code/lib3.py](code/lib3.py) supplies exact definitions. [code/verify_all.py](code/verify_all.py) tests formulas and grouping; [code/lemma6_check.py](code/lemma6_check.py) checks the accounting; [code/verify_csf.py](code/verify_csf.py) compares small graph expansions. [code/review_regressions.py](code/review_regressions.py) protects the review repairs and runs four deliberate failing expectations in normal/optimized modes. [checks/review-regressions.md](checks/review-regressions.md) records actual regression results; [REPLAY_RECEIPT.md](REPLAY_RECEIPT.md) records main-run coverage.

## Limits and provenance

[reviews/revision-response.md](reviews/revision-response.md) maps revisions. [STATUS.md](STATUS.md), [PROVENANCE.md](PROVENANCE.md) and [LICENSES.md](LICENSES.md) define status, roles and rights. No formal verification, external peer-review status, definitive novelty proof, four-star rating, or completed public publication is implied. Code success is not proof adequacy; hashes bind bytes only.
