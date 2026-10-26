# Biquaternion decompositions — the algebra alone, then the forms

Internal note. It is not an article, it is not a plan, and it changes no corpus file.

**Last updated:** 2026-09-27.

**The order of the file.** The decompositions of the algebra come first (§1), because they
are prior to any form: they use the product, the coefficient of $e_t$, and the
characteristic polynomial. Then the four forms and their norms (§2). Then the
decompositions that use a form (§3–§7). Then the queue (§8).

**The cut.** A form on $\mathbb{B}$ is the scalar part of a product: every one of the four
forms is $\operatorname{Sc}$ applied to $x\,c(y)$, where $c$ is a conjugation on the second
slot. So a decomposition either evaluates the scalar part or it does not. If it does not,
it uses no form, and it is in §1. If it does, it uses exactly one of the four forms, and it
is in §3–§6. That is the first and only cut.

**Status vocabulary.** `covered` = the corpus already has it, do not duplicate. `ready` =
statement and anchors fixed, the article can be written. `research` = the theorem is not
checked, do not write from the note. `optional` = adjacent, write last. `rejected` = not
worth an article, reason given.

**Update protocol.** Move an entry between sections only if its use of the scalar part
changes, which requires a proof. Change a status in place, and add a line to §10.

## 0. The answer in one page

This is the short answer; §1–§8 are the evidence. Status words are those of the header:
`covered` (used in the corpus), `ready` (statement fixed, article can be written),
`research` (theorem not checked), `optional`, `rejected`.

**The order rule.** An entry may be written only after the article that introduces every
notion it uses. The positions below are the article positions of the biquaternion algebra
block, after the two menu moves of 2026-09-27. The first polar is article 45; the first
N-polar is article 55; K-regularity is article 66. No entry is placed before its
prerequisite.

### 0.1 Used in the corpus

| Decomposition | Form | Article (position) |
|---|---|---|
| Peirce at an idempotent | none | *The Peirce Decomposition* (15) |
| Jordan–Chevalley additive | none | *The Semisimple–Nilpotent Split* (30) |
| Eigenvalue decomposition | none | *The Spectrum* (24); *The Eigenbasis* (31); *The Jordan Normal Form* (34) |
| Scalar–vector, quaternion and Hermitian eigenspace splits | none | *The Three Eigenspace Decompositions* (6) |
| Zero divisor as one Peirce corner | none | *Zero Divisors and Units* (10); *Nilpotents* (13); *Idempotents* (14) |
| Regular-module split | none | *The Regular Module* (21) |
| Spinor spaces and the two couples | none | *The Spinor Spaces* (16) |
| Minimal left ideals | none | *The Minimal Left Ideals* (22) |
| $M_2$ block form / $M_4$ block form | none | the two matrix-product articles (11, 12) |
| $H$-polar, general and Cartan | H | *The Polar Decomposition of a Biquaternion* (45) |
| $H$-spectral (normal, unitary eigenbasis) | H | *The Biquaternion Eigenvalue Decomposition* (Clifford block); *$M_2(\mathbb{C})$ Representation : The Eigenbasis and the Diagonalising Matrix* (32) |
| $H$-SVD at matrix level | H | *$M_2(\mathbb{C})$ Representation : The Polar Decomposition of a Matrix* (46) |
| Modulus–unit $Q=\Rho U$ and the four-factor word | N + H | *The Polar Decomposition of an N-Regular Biquaternion* (55) |
| Exponential polar | N + H | the exponential-polar series (99–121) |
| Krein isometry group and Cartan decomposition | K | *The Krein Isometry Group and Its Cartan Decomposition* |

### 0.2 Suggested by the corpus, not implemented

**None.** The corpus names no decomposition that it does not either write or defer to an
article that exists. The four-factor refinement is in (55); the exponential polar is in
the exponential-polar articles; the spectral decomposition is in (31) and (34); the
multiplicative Jordan–Chevalley is in (30); the Moore–Penrose inverse is in
*The Moore–Penrose Inverse in an Involutive Algebra*, cited by (45). Everything in §0.3
is an extension, not a corpus suggestion.

### 0.3 Extensions, not in the corpus

These are new mathematics. No article names them, so none is a "suggestion"; each is a
possible addition, placed after the article that introduces its ingredients.

| Decomposition | Form | Status | Earliest position | Note |
|---|---|---|---|---|
| Algebraic polar $M=US$, $U\in O(2,\mathbb{C})$, $S^{\mathsf T}=S$ | N | ready | after 54 | §8.2 |
| Complex-orthogonal SVD | N | research, low | after 54 | §8.5 |
| Indefinite polar $A=UP$, $U\in U(1,3)$ | K | research, high risk | after 65 | §8.3 |
| Failure of the indefinite SVD | K | research, negative | after 65 | §8.4 |
| Singular values at element level | H + N | ready | after 47 | §8.1 |

The word *polar* is not available before article 44. The algebraic and indefinite polars
are not in the corpus at all.

### 0.4 Order of writing

The file's order is the norm order of §3–§7: N, then K, then several forms. Within a
norm, polar before SVD.

1. **Algebraic polar** (N), after 54.
2. **Complex-orthogonal SVD** (N), after 54.
3. **Indefinite polar** (K), after 65.
4. **Failure of the indefinite SVD** (K), after 65.
5. **Singular values at element level** (H + N), after 47; cheapest, but a hybrid, so
   it sits in §7.

### 0.5 Possible and not possible

- **Possible at element level:** (1), (2), (5).
- **Possible at operator level:** (3) under a checked spectral hypothesis; (4) as a
  counterexample article, never as a positive theorem.
- **Not possible as stated:** $K$-spectral (false: $L_{\vec e_x}$ is $K$-normal with
  spectrum $\{i,-i\}$), $K$-SVD with real singular values and a conserved inertia
  (§6), the $P$-family as new work ($S$-conjugate of $N$), and the $H$/$N$ flag
  decompositions (trivial, basis-dependent, or broken at isotropic vectors).

## 1. The form-free layer

This is the layer before the forms. It uses the product, the scalar part as a coefficient,
and the characteristic polynomial. No pairing of two vectors occurs anywhere in it. In
`maths.md` it is filed as two sections, in this order: *The Frame* (the frame, §1.1) and
*Spectral Algebra* (the element, §1.2–§1.5). The frame
comes first because it needs only an idempotent, while every spectral statement is read in
it. LU is recorded at the end and rejected: it is algebraic, not spectral, and it is
listed only to close the list.

### 1.1 Peirce: the frame

Relative to an idempotent $e$ with $f=e_t-e$,

$$
\mathbb{B}=e\mathbb{B}e\;\oplus\;e\mathbb{B}f\;\oplus\;f\mathbb{B}e\;\oplus\;f\mathbb{B}f,
\qquad
Q=eQe+eQf+fQe+fQf .
$$

The blocks are the four Peirce corners. A **complete frame** is a pair $\{e,f\}$ of
orthogonal idempotents summing to $e_t$; in $\mathbb{B}$ the four corners of a complete
frame of primitive idempotents are one-dimensional, so the Peirce coordinates are the
matrix entries of the matrix model.

Two facts used below.

- **Corner product.** $(e\mathbb{B}f)(e\mathbb{B}f)=e\mathbb{B}(fe)\mathbb{B}f=0$. Every
  element of an off-diagonal corner is square-zero.
- **Single corner.** In a complete frame, a non-zero element supported in exactly one corner
  has rank one; the corner is diagonal or off-diagonal according to whether the element is
  idempotent-like or nilpotent.

- **Corpus:** covered by *Ideals, Peirce Decompositions and Spinors in the Biquaternion
  Algebra*, *Complementary Idempotents and the Peirce Decomposition*, and the
  *Peirce Coordinates* articles of the $M_2$ and $M_4$ series.
- **Status:** covered.
- **Why it is form-free:** idempotents, corners and blocks are defined by the product.

### 1.2 The characteristic polynomial

For $Q=Q_te_t+\vec Q$, the **vector square** is the scalar

$$
B^2:=Q_x^2+Q_y^2+Q_z^2,\qquad \vec Q^2=-B^2e_t,\qquad \vec Q\times\vec Q=0 .
$$

The **characteristic polynomial** is

$$
p_Q(X)=(X-Q_t)^2+B^2 .
$$

It is intrinsic: with $Q^{\nu}=Q_te_t-\vec Q$ the conjugate, $(X-Q)(X-Q^{\nu})=p_Q(X)e_t$
is central, so $p_Q$ is the polynomial of the subalgebra $\mathbb{C}[Q]$. No determinant
and no matrix is used.

| Quantity | Value | Meaning |
|---|---|---|
| trace | $2Q_t$ | twice the scalar part |
| constant term | $Q_t^2+B^2$ | the scalar of $QQ^{\nu}$ |
| discriminant | $-4B^2$ | zero iff the two roots coincide |
| eigenvalues | $Q_t\pm iB$ | $B$ is a chosen square root of $B^2$; $i$ is internal to the algebra |
| minimal polynomial | see the table below | the four spectral types |

The four types, which organise the whole section:

| Type | Condition | $p_Q$ | $m_Q$ |
|---|---|---|---|
| scalar | $\vec Q=0$ | $(X-Q_t)^2$ | $X-Q_t$ |
| semisimple | $B^2\ne0$ | $(X-Q_t)^2+B^2$ | $=p_Q$ |
| Jordan | $B^2=0$, $\vec Q\ne0$, $Q_t\ne0$ | $(X-Q_t)^2$ | $(X-Q_t)^2$ |
| nilpotent | $B^2=0$, $Q_t=0$, $Q\ne0$ | $X^2$ | $X^2$ |

Vocabulary, matching the corpus. $Q$ is **spectrally regular** when $B^2\ne0$ and
**spectrally degenerate** when $B^2=0$. The degenerate set splits into the Jordan
type, the nilpotent type, and the scalar line, where the last is semisimple with a single
eigenvalue and is the vertex of the degenerate set.

The degree is two, the discriminant is $-4B^2$, and the four rows of the table are the
four possible minimal polynomials. Everything below is a reading of one row.

#### The matrix-free dictionary

The matrix model is a convenience, not a definition. When the model is used, the
translation is:

| matrix word | biquaternion word |
|---|---|
| determinant | $B^2$, the scalar square of the vector part |
| characteristic polynomial | $(X-Q_t)^2+B^2$ |
| rank | the type: $Q$ invertible, $Q$ a zero divisor, $Q=0$ |
| eigenvector | a spectral idempotent $\Pi_\pm$ |
| Jordan form | the Jordan pair $\vec\Upsilon_\pm$ of §1.3 |
| diagonalisation | the eigenbasis of §1.4 |

A general article in this section states its theorem in the right column and cites the left
column only as a check.

### 1.3 Jordan–Chevalley: the element in the frame

$$
Q=S+N,\qquad SN=NS,\qquad S\text{ semisimple},\quad N\text{ nilpotent}.
$$

The corpus states the tie with Peirce in the split case:

$$
Q=\sum_i\bigl(\lambda_i\varepsilon_i+n_i\bigr),\qquad
n_i\in\varepsilon_i\mathbb{B}\varepsilon_i,\qquad n_i^{e_i}=0 .
$$

The $\varepsilon_i$ are the spectral idempotents; in the Jordan algebra literature they are
the **Peirce idempotents** of $Q$. They are the projections onto the generalized
eigenspaces. The Peirce decomposition at the frame $\{\varepsilon_i\}$ organizes the
algebra by those subspaces: the diagonal block $\varepsilon_i\mathbb{B}\varepsilon_i$ is
the endomorphism algebra of the $i$-th generalized eigenspace, and the off-diagonal block
$\varepsilon_i\mathbb{B}\varepsilon_j$ maps the $j$-th into the $i$-th. Each $n_i$ is
the nilpotent part **inside** the diagonal block. So:

- **Peirce** is the resolution of the algebra at the frame of the semisimple part;
- **Jordan–Chevalley** is the splitting of the element inside the diagonal blocks;
- **eigen** is the case $n_i=0$ for every $i$.

They are three readings of one resolution, not three nested theorems. The corpus says it in
two places: *The Eigenvalue Decomposition in a Jordan Algebra* calls the spectral
idempotents "the spectral idempotents or Peirce idempotents", and *Nilpotent Elements and
the Jordan–Chevalley Decomposition* says the $n_i$ are "the nilpotent parts inside the
blocks".

In $\mathbb{B}$ the degree is two, and the Peirce corner pattern computed in a frame
adapted to $Q$ is the Jordan form of $Q$. Five rows, from the general element to the
degenerate elements:

| Type | Condition | Frame | Non-zero Peirce corners | JC |
|---|---|---|---|---|
| scalar | $\vec Q=0$ | $\{e_t\}$ | one diagonal | $S=Q$, $N=0$ |
| semisimple, unit | $B^2\ne0$, $QQ^{\nu}\ne0$ | spectral $\{\Pi_+,\Pi_-\}$ | two diagonal | $S=Q$, $N=0$ |
| semisimple, zero divisor | $B^2\ne0$, $QQ^{\nu}=0$ | spectral $\{\Pi_+,\Pi_-\}$ | one diagonal | $S=Q$, $N=0$ |
| Jordan | $B^2=0$, $\vec Q\ne0$, $Q_t\ne0$ | $\{e,f\}$ with $N\in e\mathbb{B}f$ | two diagonal and one off-diagonal | $S=Q_t$, $N=\vec Q$ |
| nilpotent | $B^2=0$, $Q_t=0$, $Q\ne0$ | $\{e,f\}$ with $Q\in e\mathbb{B}f$ | one off-diagonal | $S=0$, $N=Q$ |

Read the table as the Jordan form in Peirce coordinates: the diagonal corners carry the
semisimple part, the off-diagonal corner carries the nilpotent part, and the pattern of
non-zero corners, together with the scalar part, gives the type. The corner pattern is a normal form, not a frame-independent
count: the frame is chosen from $Q$. The invariant content is the JC pair, and in
$\mathbb{B}$ the pair and the type determine each other.

The last three rows are the degenerate ones. In the Jordan and nilpotent rows there is no
spectral frame, because the element is defective; the frame $\{e,f\}$ that exhibits $N$
off-diagonal is an extra choice and is not unique. JC is canonical, Peirce needs a frame,
and in the semisimple rows the spectral frame supplies it. The spectral Peirce
decomposition is a case of JC; a general Peirce decomposition needs an arbitrary idempotent
and is the frame in which JC is stated.

- **Corpus:** covered by *Nilpotent Elements and the Jordan–Chevalley Decomposition* (the
  generalized eigenvalue section) and *The Jordan–Chevalley Decomposition of a Matrix*; the
  biquaternion implementation is *The Jordan–Chevalley Decomposition of a Biquaternion*.
- **Status:** covered, including the multiplicative version $Q=SU$ for units in
  §*The Multiplicative Form* of that article.
- **Why it is form-free:** semisimplicity, nilpotency and the scalar part are properties of
  the product.

### 1.4 The semisimple case: the eigenvalue decomposition

For $B^2\ne0$,

$$
Q=\lambda_+\tilde\Pi_++\lambda_-\tilde\Pi_-,\qquad
\lambda_\pm=Q_t\pm iB,\qquad
\tilde\Pi_\pm=\tfrac12(e_t\pm\vec\Xi),\qquad
\vec\Xi=-i\vec Q/B .
$$

The two projectors are the spectral idempotents, complementary and primitive. In their
Peirce frame, $Q$ occupies the two diagonal corners and the off-diagonal corners vanish;
that is the $n=0$ row of §1.3.

- **Corpus:** covered by *The Biquaternion Eigenvalue Decomposition*, the eigenbasis
  articles, and *The Eigenvalue Decomposition in a Clifford Algebra* for the general
  dictionary.
- **Status:** covered.
- **Degenerate cases.** $B^2=0$, $\vec Q\ne0$: no eigenvalue decomposition, and no
  two-projector frame; the replacement is the Jordan basis. $B^2=0$, $\vec Q=0$: the
  one-term decomposition is unique but the two-projector refinement is not.

### 1.5 The zero divisors: a single Peirce corner

$$
QQ^{\nu}=0,\qquad Q\ne0 .
$$

The condition is intrinsic: the conjugate product vanishes, so $Q$ is a zero divisor.
Cayley–Hamilton gives $Q^2=2Q_tQ$ on this set. The two cases are the two corners:

- $Q_t\ne0$: $Q/(2Q_t)$ is an idempotent, $B^2=Q_t^2\ne0$, and $Q$ is supported in
  one **diagonal** corner. This is the semisimple zero-divisor row of §1.3.
- $Q_t=0$: $Q^2=0$, and $Q$ is supported in one **off-diagonal** corner, by the corner
  product of §1.2. This is the nilpotent row.

Conversely, every non-zero element of a single corner is a zero divisor. So the zero-divisor
set is exactly the set of single-corner configurations, and the two kinds of zero divisor
are the two kinds of corner. In the matrix model they are the rank-one matrices, which is
why the word "rank" appears in the corpus; the biquaternion statement needs no rank.

- **Corpus:** covered by *N-Regularity and N-Degeneracy*, *Square Roots of One and the
  Idempotents*, *Square Roots of Zero and the Nilpotents*, and the $M_2(\mathbb{C})$
  *Rank-One Matrices* article for the model.
- **Status:** covered. General rank factorization is rejected: in $2\times2$ it is this
  case plus the identity.
- **Why it is form-free:** $QQ^{\nu}=0$ is a product identity, not a pairing.

### 1.6 LU: rejected

$$
Q=LU,\qquad L\text{ unit lower triangular},\quad U\text{ upper triangular}.
$$

- **Status:** rejected.
- **Why:** it needs a chosen basis, the pivots are arbitrary, and in $2\times2$ it is one
  division. It carries no biquaternion content and no spectral information: it reads no
  eigenvalue, no rank and no idempotent.
- **Placement:** it is not part of the spectral layer. It is recorded here only because it
  is algebraic, and it is rejected on the same line.

### 1.7 The dependencies

| Item | Decomposes | Frame | Available when | Relation to the others |
|---|---|---|---|---|
| characteristic polynomial | — | none | always | the root; every row below reads it |
| Peirce | the algebra | an idempotent $e$ | any idempotent | the frame in which JC and eigen are stated |
| Jordan–Chevalley | the element | spectral frame of $S$ | always | Peirce plus a nilpotent inside each diagonal block; trivial in the semisimple rows |
| eigenvalue | the element | spectral frame | $B^2\ne0$ | JC with $N=0$; Peirce with zero off-diagonal |
| zero divisors | the element | one corner | $QQ^{\nu}=0$, $Q\ne0$ | one non-zero corner; the nilpotent case is JC with $S=0$ |
| LU | the matrix | a basis | always | non-spectral; rejected |

The natural first guess is half right, and the half that is wrong is worth stating.

- **Eigen is a case of Peirce.** True: Peirce at the spectral frame with the off-diagonal
  blocks zero.
- **A zero divisor is a case of Peirce.** True: a single non-zero corner.
- **Peirce and Jordan–Chevalley: the tie is real, and it cuts both ways.** Peirce at an
  arbitrary idempotent is not a case of JC, because the frame is extra data. But Peirce at
  the spectral frame of the semisimple part is the algebra-level form of the generalized
  eigenspace decomposition, and that is exactly the JC theorem: the $\varepsilon_i$ are at once the spectral and the
  Peirce idempotents, and JC is the splitting inside the diagonal blocks. So the spectral
  Peirce decomposition is a case of JC, while the general Peirce decomposition is the frame
  in which JC is stated.

A compact reading: the characteristic polynomial decides which rows exist, the Peirce frame
is the coordinate system, JC is the invariant content, eigen is the semisimple row, and
a zero divisor is the one-corner row.

### 1.8 The layer in one table

| Item | Shape | Corpus | Status |
|---|---|---|---|
| characteristic polynomial | root | yes | covered |
| Peirce at an idempotent | frame | yes | covered |
| Jordan–Chevalley additive | frame + nilpotent | yes | covered |
| Jordan–Chevalley multiplicative | frame + unit | yes | covered, JC article §*The Multiplicative Form* |
| Eigenvalue decomposition | diagonal Peirce | yes | covered |
| Zero divisors, two kinds | single corner | yes | covered |
| Rank factorization $CF$ | product | partly | rejected (matrix notion) |
| LU / LUP | elimination | no | rejected, non-spectral |

### 1.9 The article ladder: general to special

Two rules fix the order.

- **Peirce first.** Peirce needs only an idempotent and decomposes the algebra; it carries
  no spectral hypothesis on the element. Jordan–Chevalley chooses the spectral idempotents
  of the semisimple part and asserts a normal form in that frame. So JC is Peirce plus a
  special frame plus a theorem. The general frame comes first.
- **In $\mathbb{B}$, JC is thin.** $B^2\ne0$ gives $(Q,0)$; $B^2=0$ gives
  $(Q_t,\vec Q)$. Two outcomes. Peirce supplies the four corners, the minimal ideals and
  the spinors. JC is not the general theory here; Peirce is.

The ladder below is the one actually filed, after the corpus was inspected. Three entries
of the earlier draft were dropped because the corpus already owns them.

| # | Article | Role | Depends on | Status |
|---|---|---|---|---|
| 0 | *Ideals, Peirce Decompositions and Spinors in the Biquaternion Algebra* | the general frame, any idempotent | — | existing; **moved to its own section**, before the spine |
| 1 | *Spectral Regularity and Degeneracy in the Biquaternion Algebra* | the element, the polynomial, the four types | — | **existing; patched, not created**: intrinsic criterion, four-row table |
| 2 | *The Jordan–Chevalley Decomposition of a Biquaternion* | the split, the types, the Peirce corner pattern, the multiplicative form | 0, 1 | **created** |
| 3 | *The Spectrally Regular Sector and Construction of the Eigenbasis of a Biquaternion* | the semisimple case, $B^2\ne0$ | 0, 2 | existing; kept in *Spectral Algebra* |
| 4 | *The Spectrally Degenerate Sector and Construction of the Jordan Basis of a Biquaternion* | the defective case, $B^2=0$ | 0, 2 | existing; kept in *Spectral Algebra* |
| 5 | *The Zero Divisors of a Biquaternion* | one corner; the stratum $QQ^{\nu}=0$ | 0 | **dropped as an article**: the corner reading is §*The Peirce Form* of 2 and the stratum is *N-Regularity and N-Degeneracy* |
| 6 | *The Spectral Stratification of the Biquaternion Algebra* | the summary, the four sectors | 1–5 | **dropped**: the four sector articles and *Relations between Quaternionic Norm and Spectral Regularity* already are the stratification |
| 7 | *Worked Examples of Eigenbasis of a Biquaternion* | the eight standard elements | 3, 4 | existing; kept last in *Spectral Algebra* |

Reading order: 0 → 1 → 2 → 3 and 4 in parallel → 7. Entries 5 and 6 are not files.

Why the order is forced.

- 1 defines semisimple and nilpotent, which 2 uses. It also owns the four-row table.
- 2 uses the frame of 0. A spectral frame before the general frame would be a circle.
- 3 is the generic case: $B^2\ne0$ is open and dense.
- 4 is the discriminant locus: $B^2=0$, the measure-zero case.
- 7 checks 3 and 4 on the eight standard elements.
- The zero-divisor and stratification material is not a separate step: it cuts across 3 and
  4, and the corpus already has it in *N-Regularity* and in the four sector articles.

Dropped from the earlier draft, with the reason.

- **A separate characteristic-polynomial article.** *Spectral Regularity and Degeneracy*
  already is that article. It was patched instead: the criterion is now proved by
  $aa^{\natural}=(a_t^2+B^2)e_t$, the determinant of $\mathsf M_2$ is a remark and a
  check, and the four minimal-polynomial rows were added. Splitting it would have produced
  two articles with the same theorem.
- **The zero-divisor article.** The set is $QQ^{\nu}=0$, the origin and the two strata;
  *N-Regularity and N-Degeneracy* proves all of it. The only new piece is the Peirce
  corner reading, and that is a section of 2.
- **The stratification synthesis.** *Relations between Quaternionic Norm and Spectral
  Regularity and Degeneracy* plus the four sector articles already carry the joint
  norm–spectrum table. A sixth article would repeat it.
- **Spectral idempotents as an article.** They are a section of 2. The halving map,
  $\Pi_\pm$ and the branch are in *Square Roots of One and the Idempotents*.
- **JC as a long article.** It is short, because in $\mathbb{B}$ it is the
  scalar–vector split plus the statement that the spectral idempotents are Peirce
  idempotents.

**Filing.** Superseded for the form-free block by `articles_reserve/STRUCTURE-ALGEBRA.md`.
The block is four sections: *The Algebra* (12 articles), *The Frame* (8), *The Modules*
(3), *The Element* (12 and the worked examples). The forms block follows.

Rules for the ladder.

- **No determinant, no rank, no matrix in the title or the statement.** The matrix model is
  a check, cited at the end of each article, never the definition.
- **The minimal polynomial is the organiser.** Article 1 owns it; article 2 reads its four
  rows; 3 and 4 are the two spectral cases; the zero-divisor sub-case is the semisimple
  case with one zero eigenvalue.
- **One decomposition per article.** Do not merge 3 and 4: they are the two normal forms,
  and their contrast is the point.
- **The four sector articles stay where they are.** They carry the joint norm–spectrum
  stratification and are not part of the spectral spine. The strata section cites them.
- **The Clifford article** (*The Biquaternion Eigenvalue Decomposition*) is the
  Clifford-algebra reading. It stays in the Clifford section and is cited, not moved.

## 2. The forms and their algebraic norms

The decompositions of §3–§7 rest on four forms. This section holds their data once, so the
family sections do not repeat it. It is a digest of the technical note's §1, §2, §11A,
§11C, §12 and §13, and it adds no theorem.

### 2.1 The four forms are the scalar part

**Determinant versus form.** §1 used $\det Q$ and never a pairing. The form $N$ agrees with
$\det$ on the diagonal, $N(Q)=\det Q$, but the two are different objects: $\det$ is a
polynomial invariant of the product and is multiplicative, while $N(x,y)$ is a pairing of
two elements. §1 needs only the first.

Write $x=x_t+\vec x$, $y=y_t+\vec y$, $\operatorname{Sc}(x)=x_t$, and $\tau(x)=x_t-\vec x$,
$x^{*}=\overline{x_t}+\overline{\vec x}$. Then, with the product of $\mathbb{B}$,

$$
\begin{aligned}
P(x,y)&=\operatorname{Sc}(xy) &&= x_ty_t-(\vec x,\vec y),\\
N(x,y)&=\operatorname{Sc}(x\,\tau y) &&= x_ty_t+(\vec x,\vec y),\\
K(x,y)&=\operatorname{Sc}(x\,y^{*}) &&= x_t\overline{y_t}-(\vec x,\vec y)_{\bar{}},\\
H(x,y)&=\operatorname{Sc}\bigl(x\,(\tau y)^{*}\bigr) &&= x_t\overline{y_t}+(\vec x,\vec y)_{\bar{}}.
\end{aligned}
$$

Read the second column as two binary choices on the second slot. The star decides bilinear
versus sesquilinear; $\tau$ decides Gram $E$ versus Gram $I$.

| | no star: bilinear | star: sesquilinear |
|---|---|---|
| no $\tau$ | $P=\operatorname{Sc}(xy)$, Gram $E$ | $K=\operatorname{Sc}(xy^{*})$, Gram $E$ |
| $\tau$ | $N=\operatorname{Sc}(x\tau y)$, Gram $I$ | $H=\operatorname{Sc}(x(\tau y)^{*})$, Gram $I$ |

The Gram matrices and signatures:

| Form | Gram | Signature on $\mathbb{R}^8$ | Multiplicative | Definite |
|---|---|---|---|---|
| $P$ | $E$ | $(4,4)$ | no | no |
| $N$ | $I_4$ | $(4,4)$ | yes | no |
| $K$ | $E$ | $(2,6)$ | no | no |
| $H$ | $I_4$ | $(8,0)$ | no | yes |

On the diagonal,

$$
P(Q)=Q_t^2-\lvert\vec Q\rvert^2,\quad
N(Q)=Q_t^2+\lvert\vec Q\rvert^2,\quad
K(Q)=\lvert Q_t\rvert^2-\lvert\vec Q\rvert^2,\quad
H(Q)=\lvert Q_t\rvert^2+\lvert\vec Q\rvert^2 .
$$

Four facts that drive everything below.

- Only $N$ is multiplicative, and $N(Q)=\det\mathsf{M}_2(Q)$.
- Only $H$ is definite, and $H(Q)=\lVert\mathsf{M}_2(Q)\rVert_F^2/2$ on the matrix image.
- No form is both, by the zero divisors of §2.4.
- $P$ is the scalar part of the plain product, with no conjugation at all. That is what
  makes it the first form, and why a decomposition that never takes a scalar part is
  earlier still.

Note on the slot convention. The technical note puts $\tau$ on the first slot,
$P=N\circ(\tau\otimes\mathrm{id})$. The table above puts it on the second. The two agree
because $\tau$ is an anti-automorphism:
$\operatorname{Sc}(\tau x\cdot\tau y)=\operatorname{Sc}(\tau(yx))=\operatorname{Sc}(yx)=\operatorname{Sc}(xy)$.

### 2.2 Adjoints, isometry groups, dimensions

| Form | Adjoint | Isometry group | $\dim_\mathbb{R}$ | Self-adjoint means |
|---|---|---|---|---|
| $P$ | $A^{\#_P}=EA^{\mathsf T}E$ | $O_4(\mathbb{C})$ | 12 | $E$-symmetric |
| $N$ | $A^{\#_N}=A^{\mathsf T}$ | $O_4(\mathbb{C})$ | 12 | symmetric |
| $H$ | $A^{\#_H}=A^{*}$ | $U(4)$ | 16 | Hermitian |
| $K$ | $A^{\#_K}=EA^{*}E$ | $U(1,3)$ | 16 | K-self-adjoint |

$\operatorname{Isom}(P)=\{A:A^{\mathsf T}EA=E\}$ and
$\operatorname{Isom}(N)=\{A:A^{\mathsf T}A=I\}$ are conjugate by
$S=\operatorname{diag}(1,i,i,i)$, not equal: $A\in\operatorname{Isom}(P)\iff
SAS^{-1}\in\operatorname{Isom}(N)$. Both are isomorphic to $O_4(\mathbb{C})$, and the
adjoints differ. An $N$-theorem and its $P$-twin have the same group type and still read
differently in a fixed basis.

$K$ is an operator-level form: the element-level $K$-isometries are only the central
phases $U(1)$. $H$ has the element-level group $U(\mathbb{B})\cong U(2)$. $N$ has
$\{N=1\}\cong SL_2(\mathbb{C})$, whose intersection with the transpose isometries is
$O(2,\mathbb{C})$.

### 2.3 The four involutions

| Involution | Fixed space | Form |
|---|---|---|
| $A\mapsto A^{*}$ | Hermitian matrices | $H$ |
| $A\mapsto EA^{*}E$ | K-self-adjoint matrices | $K$ |
| $A\mapsto A^{\mathsf T}$ | symmetric matrices | $N$ |
| $A\mapsto EA^{\mathsf T}E$ | $E$-symmetric matrices | $P$ |

**Caution.** The technical note calls these four "the real forms of $M_2(\mathbb{C})$".
Strictly they are four anti-linear involutions, and their fixed spaces are real vector
spaces, not subalgebras: the Hermitian matrices are not closed under multiplication. The
count of four is a count of involutions, not of real forms in the algebraic sense.

### 2.4 The engine

| | definite | not definite |
|---|---|---|
| multiplicative | empty, by the zero divisors | $N$: algebra structure |
| not multiplicative | $H$: topology | $K$: indefinite geometry |

The empty cell is why there are four forms and not one. In a division algebra it is
occupied, the two properties do not separate, and a single norm serves both the algebra
and the topology. Here they separate, and each occupied cell gives one form.

Two precisions.

- "Unique survivor of the cell" holds up to normalisation. Any positive multiple of $H$ is
  also definite and not multiplicative. The canonical choices are fixed by
  $N(Q)=\det\mathsf{M}_2(Q)$ and $H(Q)=\lVert\mathsf{M}_2(Q)\rVert_F^2/2$.
- $P$ is outside the table because it is neither multiplicative nor definite. It is still a
  form, the corner of §2.1 with no conjugation at all, and it is not a fourth cell: it is
  the plain product on which the other three are read. Its metric decompositions are not
  new; they are the N-decompositions in the $S$-basis (§3).

### 2.5 The conjugations

$$
S=\operatorname{diag}(1,i,i,i),\qquad S^{\mathsf T}ES=I_4,\qquad S^{*}=S^{-1},\qquad E=S^2 .
$$

$$
N=P\circ(\mathrm{id}\otimes\tau),\qquad K=H\circ(\tau\otimes\mathrm{id}),
$$

The first identity is the definition of $N$ from the plain product: $N$ is $P$ with $\tau$
in the second slot. It also reads $P=N\circ(\tau\otimes\mathrm{id})$, because $\tau$ may
be moved from one slot to the other under $\operatorname{Sc}$; the primary object is $P$,
and $N$ is its $\tau$-twist.

$$
A^{\#_P}=S^{-1}\bigl(SAS^{-1}\bigr)^{\#_N}S,\qquad
A^{\#_K}=S^{-1}\bigl(SAS^{-1}\bigr)^{\#_H}S .
$$

Hence $A\in\operatorname{Isom}(P)\iff SAS^{-1}\in\operatorname{Isom}(N)$, and
$A\in\operatorname{Isom}(K)\iff SAS^{-1}\in\operatorname{Isom}(H)$.

Three consequences.

- Every $P$-metric item is an $N$-item conjugated by $S$. That is why §3 keeps the form
  but rejects its decompositions as separate articles.
- The same conjugation sends $K$-normal to $H$-normal, whose diagonal is complex. The
  note's K-spectral wants a real diagonal with signs; $K$-normality does not give one, and
  neither does $K$-self-adjointness. The matrix $C$ of §6 is $K$-self-adjoint with
  eigenvalues $\pm i\sqrt3$. This is the structural reason behind the $L_{\vec e_x}$
  counterexample of §6.
- On $Q\in\mathbb{R}^4$ the coefficientwise conjugation is the identity, so $P=K$ and
  $N=H$: the two bilinear forms and the two sesquilinear forms coincide in pairs. Four
  forms collapse to two, and the four-fold theory is genuinely complex. (The note pairs
  them the other way, $P=N$ and $H=K$; that is wrong, since $P$ and $N$ differ by the
  sign of the vector part on every non-pure element.)

### 2.6 The four shapes, once a form is fixed

| Shape | Canonical form | $N$ | $H$ | $K$ | $P$ |
|---|---|---|---|---|---|
| polar | $Q=US$ | algebraic polar | polar | conditional polar | $=N$ |
| spectral | $Q=VDV^{-1}$ | symmetric + diagonalizable | normal | fails as stated | $=N$ |
| SVD | $Q=UDV'$ | generic, isotropic obstruction | always | fails | $=N$ |
| flag | $Q=UTU'$, $QR$, $LL^{*}$ | conditional | always | conditional | $=N$ |

The four shapes are one schema, cut at different points. The polar keeps one factor
symmetric; the spectral makes the middle factor diagonal and one side trivial; the SVD
makes the middle diagonal and keeps both sides; the flag makes the middle triangular.

The no-form layer of §1 has its own four shapes — additive, frame, diagonal Peirce,
elimination — and they do not fit this table, because they do not use a form.

### 2.7 The relations between the shapes

| Relation | Domain | Data | Example |
|---|---|---|---|
| restriction | shrinks | same | eigen $\to$ H-spectral, by normality |
| coarsening | grows | lost | H-spectral $\to$ SVD $\to$ polar |
| refinement | same | more factors | polar $\to$ word, when $N\ne0$ |

The main chain is a zigzag, not a tower of inclusions:

$$
\text{eigen}\;\xrightarrow{\text{restriction}}\;\text{H-spectral}\;\xrightarrow{\text{coarsening}}\;\text{SVD}\;\xrightarrow{\text{coarsening}}\;\text{polar}.
$$

Going right loses information and gains domain. Going left gains information and loses
domain. No member is "more general" in both senses at once.

The composite arrow not in the chain is

$$
\text{SVD}=\text{polar}\circ\text{spectral}(P).
$$

It is a composition, not an inclusion. It holds when the spectral step holds. This is why
the K-SVD is blocked: the spectral step fails before the composition starts.

### 2.8 Why a cell is empty

| Form | Cone | Orthonormal eigenbasis | Ordering |
|---|---|---|---|
| P | no; $P$ is not definite | no; eigenvectors are not $P$-orthogonal | only with a chosen basis |
| N | no; only symmetry | for symmetric and diagonalizable, no isotropic eigenvector | conditional |
| H | yes, positive | for normal | yes |
| K | conditional, $J$-positive | no | conditional |

- No cone: the polar shape degenerates to an algebraic factorization. That is the
  $N$-polar, and it is also why $P$ has no polar of its own.
- No orthonormal eigenbasis: the spectral and SVD shapes fail. That is $K$.
- No ordering: the flag shape is the only one that needs it, and it is basis-dependent.

### 2.9 The decision rule

| Question | Form | §  |
|---|---|---|
| No scalar part at all: what is the algebra doing? | none | 1 |
| A scalar part in the plain basis, no conjugation? | $P$ | 3 |
| What is the distance? Is the algorithm stable? | $H$ | 4 |
| Is $Q$ invertible? What is the algebra structure? | $N$ | 5 |
| What is the inertia? Which directions are null? | $K$ | 6 |

## 3. $P$ — the scalar part of the plain product

$P$ is exactly the case of §2.1 with no conjugation:

$$
P(x,y)=\operatorname{Sc}(xy),\qquad P(Q)=\operatorname{Sc}(Q^2)=Q_t^2-\lvert\vec Q\rvert^2 .
$$

So $P$ is the plain product read through the scalar pairing: no conjugation enters, and
$N$ plays no part in its definition. The distinction is the whole reason §1 exists: a
decomposition that multiplies but never takes a scalar part is form-free, while a
decomposition that evaluates $\operatorname{Sc}(xy)$ uses $P$.

### 3.1 Data

$$
\operatorname{Gram}(P)=E,\qquad A^{\#_P}=EA^{\mathsf T}E,\qquad
\operatorname{Isom}(P)=O_4(\mathbb{C}),\qquad \dim_\mathbb{R}=12 .
$$

### 3.2 Its decompositions

With $S=\operatorname{diag}(1,i,i,i)$ and $S^{\mathsf T}ES=I_4$,

$$
\text{N-polar}(A)=S\,\text{P-polar}(S^{-1}AS)\,S^{-1},
$$

and the same change carries P-spectral to N-spectral and P-SVD to N-SVD. The dictionary
runs in this direction on purpose: $P$ is the plain product and needs no conjugation, while
$N$ is $P$ with $\tau$ inserted in the second slot. $P$ is the base and $N$ is the
$\tau$-twist; $P$ is not a shadow of $N$.

| Item | Form | Status |
|---|---|---|
| P-polar | $P$ | covered by the N-polar in the $S$-basis |
| P-spectral | $P$ | covered by N-spectral in the $S$-basis |
| P-SVD | $P$ | covered by N-SVD in the $S$-basis |

- **Status of the whole section:** no new article. The $S$-change is explicit and
  invertible, so each P-decomposition is the P-reading of an N-decomposition; the change is
  not an algebra automorphism, so the two are different statements, but neither needs its
  own construction.
- **Why keep the section:** because $P$ is the first form, the one with no conjugation at
  all, and because the coefficient basis is $H$-orthonormal but not $P$-orthonormal. A
  formula that looks basis-free can be a $P$-statement in disguise.

### 3.3 $P$ in one table

| Item | Shape | Corpus | Status |
|---|---|---|---|
| Modulus–unit, in $P$-coordinates | polar (algebraic) | no | covered by §5 in the $P$-basis |
| P-polar | polar | no | covered by §5 in the $P$-basis |
| P-spectral | spectral | no | covered by §5 in the $P$-basis |
| P-SVD | SVD | no | covered by §5 in the $P$-basis |
| P-QR, P-Schur | flag | no | covered by §5 in the $P$-basis |

## 4. $H$ — the definite form

$H(x,y)=\operatorname{Sc}(x(\tau y)^{*})$: both $\tau$ and star, hence sesquilinear,
positive definite, Gram $I_4$.

What the form supplies: a positive cone, a topological norm, an orthonormal eigenbasis for
normal elements. What it does not supply: multiplicativity.

| Item | Shape | Corpus | Status |
|---|---|---|---|
| General polar $Q=Q_HQ_0$ | polar | yes | covered |
| Cartan polar on units | polar | yes | covered |
| Four-factor word, three pairings | polar (refined) | yes | covered |
| H-spectral | spectral | yes | covered |
| H-SVD, matrix | SVD | yes | covered |
| H-SVD, element level | SVD | no | ready |
| H-QR, H-Cholesky, H-Schur | flag | no | rejected |

- **General polar.** $Q=Q_HQ_0$ with $Q_H$ positive semidefinite and $Q_0$ a partial
  isometry, on the whole algebra. Total, and both factors are functions of $Q$. Covered by
  *The Polar Decomposition of a Biquaternion*.
- **Cartan polar.** The restriction to $N\ne0$: $Q_H>0$ and $Q_0$ unitary. Covered by
  *The Polar Decomposition of a N-Regular Biquaternion*.
- **The word.** On $N\ne0$, $Q=r\zeta U_{\mathrm b}u_{\mathrm r}$. It is a refinement of
  the polar, listed in full in §7 because it also uses $N$.
- **H-spectral.** Normal $Q=V\Lambda V^{\#}$ with $V$ unitary. Normality is exactly
  $\vec Q/B$ real, not $\vec Q$ real; for $(1+i)\vec e_x$ the vector part is not real and
  the element is normal. Covered by *The Biquaternion Eigenvalue Decomposition*.
- **H-SVD, matrix.** $M=U\Sigma V^{\dagger}$ with $\Sigma$ real nonnegative. Covered by the
  $M_2$ polar article.
- **H-SVD, element level.** The two-norm formula of §7. Ready, see §8.1.
- **Flag.** Standard matrix algebra, trivial in $2\times2$. Rejected.

What $H$ cannot give: there is no $H$-analogue of the modulus–unit split, because $H$ is
not multiplicative. The $H$-polar is the strongest statement this cell supports.

## 5. $N$ — the multiplicative form

$N(x,y)=\operatorname{Sc}(x\tau y)$: $\tau$ and no star, hence bilinear, multiplicative,
Gram $I_4$, and $N(Q)=\det\mathsf{M}_2(Q)$.

What the form supplies: multiplicativity, the determinant, the invertibility criterion.
What it does not supply: a cone, a topology, a positive notion.

| Item | Shape | Corpus | Status |
|---|---|---|---|
| Modulus–unit $Q=\Rho U$ | polar (algebraic) | yes | covered |
| N-polar $M=US$ | polar | no | ready |
| N-spectral | spectral | no | research, low |
| N-SVD | SVD | no | research, low |
| N-QR, N-Schur | flag | no | rejected |

- **Modulus–unit.** $\Rho^2=N(Q)$ and $N(U)=1$, so $Q=\Rho U$ with an invertible unit.
  This is the $N$-cell's own polar-like split, and it has no positivity: $\Rho\in\mathbb{C}$
  and $U\in SL_2(\mathbb{C})$. Covered by *The Polar Decomposition of a N-Regular
  Biquaternion*, §*The Four Factors*.
- **N-polar.** $M=US$ with $U\in O(2,\mathbb{C})$ and $S$ complex symmetric. The same shape
  as the polar, with a symmetric middle factor. Covered by no article. Ready, see §8.2.
- **N-spectral.** $M$ complex symmetric and diagonalizable, eigenvalues distinct, no
  isotropic eigenvector. Research, low: it is a matrix theorem in a fixed basis.
- **N-SVD.** Same obstruction, the isotropic eigenvector. Research, low.
- **Flag.** Breaks at isotropic columns. Rejected.

The real content of this cell is negative. $N$ decides invertibility and nothing else.
Every geometric word in the corpus is $H$-language; $N$ supplies the scalar factors only.

## 6. $K$ — the indefinite form

$K(x,y)=\operatorname{Sc}(xy^{*})$: star and no $\tau$, hence sesquilinear, indefinite,
Gram $E$, signature $(2,6)$.

What the form supplies: an indefinite scalar product, a Krein signature, a conditional
$J$-positive cone. What it does not supply: an orthonormal eigenbasis.

| Item | Shape | Corpus | Status |
|---|---|---|---|
| Krein/Cartan group decomposition | group | yes | covered |
| K-polar | polar | no | research |
| K-spectral | spectral | counterexample only | rejected as stated |
| K-SVD | SVD | no | research, negative |
| K-QR, K-Schur, K-Cholesky | flag | no | rejected |

- **K-polar.** $A=UP$ with $U\in U(1,3)$ and $P$ K-self-adjoint, for invertible $A$ with
  $A^{\#K}A$ having no negative real eigenvalue. Research, see §8.3.
- **K-spectral.** False as stated. $L_{\vec e_x}$ is $J$-normal and has spectrum
  $\{i,-i\}$, each twice. Rejected.
- **K-SVD.** Blocked, not difficult: it contains the spectral step that just failed.
  Research, negative.
- **Flag.** Conditional and basis-dependent. Rejected.
- **Group level.** *The Krein Isometry Group and Its Cartan Decomposition* covers the group
  statement. At element level the K-isometries are only the central phases $U(1)$, so an
  element-level K-theory is nearly empty. $K$ is an operator-level form.

**The K-SVD counterexample.** Take $A=\begin{pmatrix}1&1\\0&1\end{pmatrix}$ and
$E=\operatorname{diag}(1,-1)$. Then $A$ is invertible and

$$
A^{\#K}A=\begin{pmatrix}1&1\\-1&0\end{pmatrix}
$$

has eigenvalues $(1\pm i\sqrt3)/2$. Embedded in $\mathbb{C}^4$ with
$E=\operatorname{diag}(1,-1,-1,-1)$, the same non-real eigenvalues survive. So
invertibility gives neither real K-singular values nor an inertia to conserve.

**The hybrid identities.** With the same $E$, the matrix
$C=\begin{pmatrix}1&2\\-2&-1\end{pmatrix}$ is K-self-adjoint, has eigenvalues
$\pm i\sqrt3$, and has H-singular values $3$ and $1$. The H-singular values are not the
moduli of the K-eigenvalues, and the two SVDs do not share singular subspaces.

The cell's invariant is the inertia $(2,6)$ of $K$. None of the K-decompositions of the
note is stated in terms of it: the note's K-SVD claims an inertia, and the counterexample
above shows that the claim fails.

## 7. Several forms at once

This is the only section where two forms appear in one statement, and it is where the real
content is.

| Item | Forms | Shape | Corpus | Status |
|---|---|---|---|---|
| Four-factor word | N + H | polar (refined) | yes | covered |
| Three pairings | N + H | polar (2-block) | yes | covered |
| Two-norm SVD | H + N | SVD | no | ready |
| Moore–Penrose | H + N | derived | no | optional |
| Takagi, element level | N + H | SVD | no | rejected |
| Hybrid SVD of the note | K + H | SVD | no | rejected |

- **The word.** On $N\ne0$,
  $$
  Q=r\,\zeta\,U_{\mathrm b}\,u_{\mathrm r}.
  $$
  The scalars $r,\zeta$ come from $N$: $r=|\Rho|$ and $\zeta=\Rho/r$ with $\Rho^2=N(Q)$.
  The factors $U_{\mathrm b},u_{\mathrm r}$ come from $H$: the Hermitian positive boost and
  the unitary rotor. The word is not a refinement of the $H$-polar alone. It needs both
  forms: $N$ for the split, $H$ for the boost and the rotor.
- **The three pairings** are the three two-block cuts of the word,
  $$
  \begin{array}{ll}
  (rU_{\mathrm b})(\zeta u_{\mathrm r}) & \text{H (polar)},\\
  (r\zeta)(U_{\mathrm b}u_{\mathrm r}) & \text{N (modulus–unit)},\\
  (ru_{\mathrm r})(\zeta u_{\mathrm r}^{-1}U_{\mathrm b}u_{\mathrm r}) & \text{H on the real form}.
  \end{array}
  $$
- **Two-norm SVD.** The factorisation is $H$: unitary times diagonal times unitary. The
  singular values are read by $N$:
  $$
  \sigma_1^2+\sigma_2^2=2H(Q),\qquad \sigma_1\sigma_2=|N(Q)|,
  \qquad
  \sigma_\pm^2=H(Q)\pm\sqrt{H(Q)^2-|N(Q)|^2}.
  $$
  One formula carries both forms, and it is the reason the element-level SVD is not a
  restatement of the matrix SVD. Ready, see §8.1.
- **Moore–Penrose.** The partial isometry is $H$-data, the rank is $N$-data. Optional,
  §8.7.
- **Takagi.** Needs $N$-self-adjointness ($M^{\mathsf T}=M$) and $H$-isometry ($V$
  unitary). At element level the symmetry condition is $Q_y=0$ in the fixed model, hence
  basis-dependent, hence rejected. At matrix level it is a theorem of the matrix series.
- **Hybrid SVDs of the note.** §8.2 and §8.3 of the note are false, with the
  counterexample of §6.

**Caution.** "Several forms" is not a fifth form. It means the factors are constrained by
different forms. The compatibility between them is the whole content, and it is exactly
where the note's errors occur. A multi-form claim must name, for each factor separately,
which form constrains it.

### 7.1 The cross table

| Item | Forms | Shape | Corpus | Status |
|---|---|---|---|---|
| Jordan–Chevalley additive | none | additive | yes | covered |
| Jordan–Chevalley multiplicative | none | additive | partly | optional |
| Eigenvalue decomposition | none | idempotent | yes | covered |
| Peirce at an idempotent | none | idempotent | yes | covered |
| Rank-one / zero divisors | none | product | yes | covered |
| Rank factorization $CF$ | none | product | partly | rejected |
| LU / LUP | none | flag | no | rejected |
| P-polar, P-spectral, P-SVD | P | all | no | rejected, $=N$ after $S$ |
| General polar, Cartan polar | H | polar | yes | covered |
| H-spectral | H | spectral | yes | covered |
| H-SVD, matrix | H | SVD | yes | covered |
| H flag: QR, Cholesky, Schur | H | flag | no | rejected |
| Modulus–unit | N | polar (algebraic) | yes | covered |
| N-polar | N | polar | no | ready |
| N-spectral | N | spectral | no | research, low |
| N-SVD | N | SVD | no | research, low |
| N flag: QR, Schur | N | flag | no | rejected |
| Krein/Cartan group | K | group | yes | covered |
| K-polar | K | polar | no | research |
| K-spectral | K | spectral | counterexample only | rejected as stated |
| K-SVD | K | SVD | no | research, negative |
| K flag: QR, Schur, Cholesky | K | flag | no | rejected |
| Four-factor word | N + H | polar (refined) | yes | covered |
| Three pairings | N + H | polar (2-block) | yes | covered |
| H-SVD, element level | H + N | SVD | no | ready |
| Moore–Penrose | H + N | derived | no | optional |
| Takagi, element level | N + H | SVD | no | rejected |
| Hybrid SVD of the note | K + H | SVD | no | rejected |

## 8. Implementation queue

| Rank | Working title | Family | Shape | Earliest position | Status |
|---|---|---|---|---|---|
| 1 | The Algebraic Polar Decomposition of an N-Regular Biquaternion | N | polar | after 54 | ready |
| 2 | The Complex-Orthogonal SVD | N | SVD | after 54 | research, low |
| 3 | The Indefinite Polar Decomposition of an Invertible Operator | K | polar | after 65 | research |
| 4 | The Failure of the Indefinite SVD | K | SVD | after 65 | research, negative |
| 5 | The Singular Values of a Biquaternion | H + N | SVD | after 47 | ready |
| — | The Multiplicative Jordan–Chevalley Decomposition of a Unit | none | additive | covered (30) | **covered** by *The Semisimple–Nilpotent Split* |

The form-free family is now closed: the additive shape is §*The Multiplicative Form*
of the JC article, and the other four shapes are covered or rejected.

### 8.1 The Singular Values of a Biquaternion

- **Family H + N, shape SVD.** Element level, $Q\in\mathbb{B}$.
- **What is new.** The matrix SVD is already in the $M_2$ polar article. The new article is
  the element-level reading: the two-norm formula, the rank criterion, the equality case,
  and the degenerate strata. It must not restate the matrix theorem.
- **Theorem.** With $M=\mathsf{M}_2(Q)$,
  $$
  \sigma_1^2+\sigma_2^2=2H(Q),\qquad \sigma_1\sigma_2=|N(Q)|,\qquad
  \sigma_\pm^2=H(Q)\pm\sqrt{H(Q)^2-|N(Q)|^2}.
  $$
  The factor $2$ is real: $\mathsf{M}_2$ is an algebra isomorphism but not an isometry,
  $\lVert M\rVert_F^2=2H(Q)$.
- **Factorisation.** Unitary biquaternions $Q_U,Q_V$ and a Hermitian positive semidefinite
  $Q_\Sigma$ give $Q=Q_UQ_\Sigma Q_V^{\#}$.
- **Rank.** $\sigma_2>0$ iff $N(Q)\ne0$; $\sigma_2=0<\sigma_1$ iff $N(Q)=0$ and $Q\ne0$.
- **Equality case.** $\sigma_1=\sigma_2$ iff $H=|N|$ iff $Q=\zeta q$ with $|\zeta|=1$ and
  $q\in\mathbb{R}^4$.
- **Worked values.** $e_t$: $(1,1)$. $e_t+e_x$: $(\sqrt2,\sqrt2)$. $e_t+i e_x$: $(2,0)$.
  $e_t+e_x+i e_y$: $(1+\sqrt2,\sqrt2-1)$. Nilpotent $e_x+i e_y$: $(2,0)$.
  $e_t+e_x+e_y$: $(\sqrt3,\sqrt3)$.
- **Risks.** Say the factor $2$. Do not call $\sigma_i$ eigenvalues. The unitary factors are
  unique only up to phases on degenerate singular subspaces.
- **Size:** 300–400 lines.

### 8.2 The Algebraic Polar Decomposition of an N-Regular Biquaternion

- **Family N, shape polar.** Element level, $N(Q)\ne0$.
- **What is new.** The corpus has only $H$-polars. Here both adjectives change: symmetric
  instead of positive, complex orthogonal instead of unitary.
- **Theorem.** With $M=\mathsf{M}_2(Q)$,
  $$
  M=US,\qquad U\in O(2,\mathbb{C}),\quad S^{\mathsf T}=S,\quad S^2=M^{\mathsf T}M.
  $$
  It exists for every invertible $M$ on a chosen branch. On the right-half-plane branch
  it exists and is unique iff $M^{\mathsf T}M$ has no negative real eigenvalue.
- **Basis dependence.** The form is fixed in the coefficient basis, and the transpose is
  the matrix transpose, not one of the four conjugations. In the fixed model,
  $S^{\mathsf T}=S$ corresponds to $Q_y=0$, which is not an invariant subspace. Say so.
- **Worked examples.** $M=\operatorname{diag}(2,3)$: $S=\operatorname{diag}(2,3)$, $U=I$.
  $M=\begin{pmatrix}0&1\\-1&0\end{pmatrix}$: $S=I$, $U=M$.
  $M=\operatorname{diag}(1,i)$: $M^{\mathsf T}M=\operatorname{diag}(1,-1)$, two branches.
- **Risks.** Do not call $S$ positive. $N(S)=\det S=\pm\det M$, so the symmetric factor
  carries the norm only up to sign. Do not confuse this with the modulus–unit split.
- **Size:** 400–500 lines.

### 8.3 The Indefinite Polar Decomposition of an Invertible Operator

- **Family K, shape polar.** Operator level, $A\in GL_4(\mathbb{C})$.
- **Gap.** Real: *J-Self-Adjoint and J-Unitary Operators* says it claims no new polar
  decomposition.
- **Correct hypothesis.** $A$ invertible and $A^{\#K}A$ with no negative real eigenvalue.
- **Research.** Check Azizov–Iokhvidov and the corpus's $J$-positive cone before writing.
- **Risk:** high. A wrong hypothesis propagates through every later K-article.

### 8.4 The Failure of the Indefinite SVD

- **Family K, shape SVD.** Operator level.
- **Content.** The counterexample of §6, the spectral condition that repairs it, and the
  comparison with the definite case.
- **Do not write it as a positive theorem.** There is none.

### 8.5 The Complex-Orthogonal SVD

- **Family N, shape SVD.** Low priority.
- **Problem.** The note's criterion is circular. The usable sufficient condition is:
  $M^{\mathsf T}M$ has distinct eigenvalues and non-isotropic eigenvectors.
- **Decision.** Parked until 8.2 is written.

### 8.6 The Multiplicative Jordan–Chevalley Decomposition of a Unit

- **Form-free, shape additive.** Covered, not to be written separately: *The
  Semisimple–Nilpotent Split*, §*The Multiplicative Form*, has the
  unit case $\tilde Q=SU$ with $U=e_t+S^{-1}N$ and the two obstructions.
- **Why optional.** The general article already has the biquaternion example, and the
  unit-group article covers the product structure.
- **Only write if it adds** the two strata $B^2\ne0$ and $B^2=0$ and the relation to the
  polar word. Otherwise skip.

### 8.7 The Moore–Penrose Inverse of a Biquaternion

- **Family H + N, derived from the SVD.** **Covered**, not a decomposition to add.
- **Where.** *The Polar Decomposition of a Biquaternion* (45) defines it, proves
  uniqueness, gives the closed form on the Hermitian factor and the three cases; the
  general theorem is *The Moore–Penrose Inverse in an Involutive Algebra*, cited there.
- **Decision.** Do not write a biquaternion article for it unless the general algebra
  article is absent; check that file before reopening this entry.

## 9. Level rule and cautions

1. **Element or operator.** $N(Q)=\det\mathsf{M}_2(Q)$ is defined for $Q\in\mathbb{B}$. For
   an operator on $\mathbb{B}$, the determinant of the $4\times4$ matrix is not $N$; for a
   left multiplication it is $N^2$. Choose the level first.

| Form | Element-level group | Operator-level group |
|---|---|---|
| none | the algebra and its units, no group from a form | — |
| P | the same as N after $S$; no separate group | $O_4(\mathbb{C})$ |
| N | $\{N=1\}\cong SL_2(\mathbb{C})$; $O(2,\mathbb{C})$ for the transpose form | $O_4(\mathbb{C})$ |
| H | $U(\mathbb{B})\cong U(2)$ | $U(4)$ |
| K | central phases $U(1)$ | $U(1,3)$ |

2. **A form is a scalar part.** Every form in this note is $\operatorname{Sc}(x\,c(y))$.
   A decomposition that never evaluates such an expression uses no form, even if it uses
   the product heavily. That is §1.
3. **$P$ is the scalar part of the plain product**, not the product. The product-only
   family of §1 is not $P$; it is prior to $P$.
4. **The determinant is not the form.** §1 writes $\det Q$ and never $N(Q)$. The form
   $N$ agrees with the determinant on the diagonal only; it is a pairing, and the
   determinant is a polynomial invariant. See §2.1.
5. **K-regular is not invertible.** The note says it, then uses K-regularity as a
   hypothesis for the K-polar. Replace it by invertibility.
6. **K-spectral is false as stated.** $L_{\vec e_x}$ is $J$-normal with spectrum
   $\{i,-i\}$.
7. **K-SVD reality is false.** §6.
8. **Hybrid SVD identities are false.** §6.
9. **N-SVD criterion is circular.** Replace it.
10. **$N(A)$ decides invertibility at element level only.** For operators, use
    $\det A\ne0$.

## 10. Changelog

- **2026-09-27 (Peirce/ideal ordering repair).** The ideal theory is no longer introduced
  in *The Peirce Decomposition*: that article now uses only the product and the
  idempotents, and the ideal definitions and the two-sided ideal theorem sit in
  *The Regular Module*. No decomposition changed; Peirce (15) remains the only Peirce row
  in §0.1.
- **2026-09-27 (used-table correction).** §0.1 now cites the actual $H$-spectral
  theorem (*The Biquaternion Eigenvalue Decomposition*, and the $M_2$ spectral theorem),
  not *The Eigenbasis*, which is the Peirce eigenbasis and works for every spectrally
  regular element. Added the three eigenspace splits (6) and the exponential polar series.
- **2026-09-27 (K-spectral correction).** §2.5 no longer says that a real signed
  diagonal needs $K$-self-adjointness. In an indefinite space $K$-self-adjointness does
  not force a real spectrum: the matrix $C$ of §6 is $K$-self-adjoint with eigenvalues
  $\pm i\sqrt3$.
- **2026-09-27 (real-restriction correction).** §2.5 no longer says $P=N$ and $H=K$ on
  $\mathbb{R}^4$. With real coefficients the star is the identity, so $N=H$ and $P=K$;
  $P$ and $N$ differ by the sign of the vector part and never coincide off the scalar
  line.
- **2026-09-27 (isometry correction).** §2.2 no longer says
  $\operatorname{Isom}(P)=\operatorname{Isom}(N)$ as sets. The two subgroups are
  conjugate by $S=\operatorname{diag}(1,i,i,i)$, not equal: a Lorentz boost preserves $P$
  and not $N$. The decomposition verdict is unchanged, since conjugacy is what makes the
  $P$-family a rewrite of the $N$-family.
- **2026-09-27 (norm-leak repair).** Removed the five premature groups from the form-free block: the determinant and quadratic signatures (7, 8, 23), the characteristic- and minimal-polynomial and Jordan language (9, 11, 12, 16, 17, 19, 21, 22), the primitivity criterion in ideal language (15), and the Euclidean unit, length and orthonormal wording (9, 13, 14, 17, 30, 31, 32). The zero-divisor tests in (19) and (23) are now written with the central scalar $Q_t^2+B^2$, and in (23) as $\tilde\Pi\tilde\Pi^{\natural}=0$. The block now names no algebraic norm, signature or form except in forward citations and in meta-sentences saying that no norm is used. Positions corrected in §0.1: zero divisors 10, matrix products 11 and 12.
- **2026-09-27:** added §0, the one-page answer: used, suggested, worth implementing, possible. It is a summary only; §1–§8 remain the evidence. Corrected the corpus status of the algebraic polar to `ready` (no article yet) and listed the $H$-SVD element level first in the queue.
- **2026-09-27:** file created.
- **2026-09-27:** rewrote the taxonomy as eight shapes in two genera.
- **2026-09-27:** restructured into "no form" and "one form".
- **2026-09-27:** split the form part by norm.
- **2026-09-27:** reclassified the product-only family as $P$-structural.
- **2026-09-27:** added the norm reference, now §2.
- **2026-09-27:** reversed the previous point. A form is the scalar part, so the
  product-only family is form-free again (§1), and $P$ gets its own short section (§3) as
  the scalar part of the plain product. Added the $\operatorname{Sc}$ table of §2.1, which
  shows the four forms as the two binary choices on the second slot. Recorded the border
  case of the eigenvalue decomposition.
- **2026-09-27:** moved the no-form layer before the forms and named it *The Spectral
  Algebra of Biquaternions* (new §1), with the forms and norms now §2. The layer runs from
  the characteristic polynomial: Peirce, Jordan–Chevalley, eigen, rank strata. LU is
  rejected as non-spectral.
- **2026-09-27:** §1 is form-free throughout: $\det Q$ replaces $N(Q)$, the matrix normal
  form $uv^{\mathsf T}$ is removed, and the rank-one stratum is defined intrinsically by
  $\det Q=0$ and split by Cayley–Hamilton.
- **2026-09-27:** corrected the Peirce/JC account. The tie is deep: the spectral
  idempotents are the Peirce idempotents, the Peirce decomposition organizes the algebra by
  the generalized eigenspaces, and JC is the splitting inside the diagonal blocks. In
  $\mathbb{B}$ the occupied Peirce corner pattern in a frame adapted to $Q$ is the Jordan
  form. Eigen is Peirce with zero off-diagonal, rank one is one non-zero corner, spectral
  Peirce is a case of JC, and general Peirce is the frame in which JC is stated.
- **2026-09-27:** §1.1 is now matrix-free. The characteristic polynomial is
  $p_Q=(X-Q_t)^2+B^2$, read off $\mathbb{C}[Q]$; the determinant is gone from the
  section. Added the four minimal-polynomial types (scalar, semisimple, Jordan, nilpotent)
  and the matrix-free dictionary. §1.5 is now *the zero divisors*, not *rank one*.
- **2026-09-27:** added §1.9, the article ladder from the general element to the special
  ones: four articles to create (characteristic polynomial, spectral idempotents, spectral
  Peirce, Jordan–Chevalley), three to move (eigenbasis, Jordan basis, worked examples),
  and the zero-divisor and stratification articles as the special and summary steps.
- **2026-09-27:** corrected the ladder order. Peirce is the general frame and comes before
  Jordan–Chevalley, which is the spectral frame plus a normal form. The spectral-idempotent
  and spectral-Peirce articles are dropped as duplicates; the JC article is short.
- **2026-09-27:** notation aligned with the corpus: $B^2=Q_x^2+Q_y^2+Q_z^2$ and
  $\vec Q^2=-B^2e_t$. The note had used $\vec Q^2$ for the scalar, which collides with
  the corpus square of the vector part.
- **2026-09-27:** ladder corrected after inspecting the corpus. *Spectral Regularity and
  Degeneracy* is the polynomial article, not a future split; it was patched in place
  (intrinsic criterion by $aa^{\natural}=(a_t^2+B^2)e_t$, determinant demoted to a check,
  four minimal-polynomial rows added). *The Jordan–Chevalley Decomposition of a
  Biquaternion* was written. The zero-divisor and stratification articles were dropped as
  duplicates of *N-Regularity* and of the four sector articles.
- **2026-09-27:** `maths.md` filed as *Spectral Algebra* (no form, after *The Products*)
  and *The Spectral Strata* (after *Algebra with the N Norm*, before Krein). The old
  *Spectral Algebra with the N Norm* is retired.
- **2026-09-27:** corrected the filing after the Peirce section was found at the end of
  *The Products*, behind the module articles. The form-free layer is now
  *The Products* → *Idempotents, Nilpotents and Square Roots* →
  *The Peirce Decomposition, Ideals and Modules* → *Spectral Algebra*. Peirce is not
  inside *Spectral Algebra*: it is the general frame, and the spectral articles are its
  particular cases, so filing it inside would invert the dependency. Entry 0 of the ladder
  is now "moved", not "cited, not moved".
- **2026-09-27:** created *Algebra with the H Norm* and moved the general polar and its two
  matrix companions into it. They sat under *Algebra with the N Norm*, but the general
  polar is the $H$-decomposition of the whole algebra and uses no $N$. The two
  N-stratified polars remain with $N$, because there the stratification is the norm.
- **2026-09-27:** wrote the new structure of the form-free block in
  `articles_reserve/STRUCTURE-ALGEBRA.md`: four sections, 34 articles, every one mapped
  to an existing file with a status (keep, rename, split, trim, new). The two form-free
  subspace articles rejoin the block, the four conjugations and the six subspaces stay
  separate, and *The Four General Products* leaves for the forms block, where it belongs.

- **2026-09-27 (execution).** The article block was written: 34 articles in four sections,
  six of them new text (the element, the square, the zero divisors, the regular module, the
  minimal left ideals, the centraliser), four split, the rest retitled. The note's §1 is
  now the four-section block; the decomposition queue of §8 is unchanged and remains the
  work that needs forms.
- **2026-09-27 (order correction).** §0 was rebuilt after a slow read of the ordered articles. It had put polar first while the first polar is article 44, and had mixed corpus suggestions with extensions that no article introduces. The queue now follows the norm order of §3–§7 with an explicit earliest position: N (after 54), K (after 65), then the hybrids. The menu was corrected in two places: the two six-subspace matrix articles now follow the matrix-product articles they assume, and the worked examples now follow the polar articles whose factors they compute. Forward uses removed from *Nilpotents* (idempotents, article 14), *The Peirce Decomposition* (the eigenbasis, articles 30/33), *The Regular Module* (spinors, article 19), and the M2 norm article (the four-factor polar and the singular values, article 44/45).
- **2026-09-27 (closed, not an issue).** *The Four General Products and Their Relations over the Biquaternion Algebra* (35) computes the four products and their four scalar parts itself, so it precedes the forms article (37) by design. The names Krein form, Hermitian form and fundamental symmetry in it label objects already displayed, and the inertia $(1,3)$ is read from the coordinate signs $\varepsilon=(1,-1,-1,-1)$. The trichotomy is a computation on the displayed scalar part and does not need article 37. Nothing is moved, nothing is rewritten.

- **2026-09-27 (spinor split).** *The Spinor Spaces* was inserted as article 16, between *The
  Peirce Decomposition* and the two Peirce-coordinate models, and the two Columns, Rows and
  Spinor Spaces articles moved from *The Modules* to *The Frame* as 19 and 20, after the
  Peirce-coordinate models. *The Frame* has eight articles and *The Modules* three; the
  positions of *The Regular Module* (21) and *The Minimal Left Ideals* (22) are the only
  §0.1 rows that moved, since the two articles removed from 22 and 23 were reinserted at
  19 and 20. The historical entries of this log keep the numbers they had when written.
