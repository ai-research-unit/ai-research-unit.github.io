# __The Four Sectors of the Reduced Biquaternion Algebra__

## Introduction

The reduced biquaternion algebra
$$
\mathbb{B}_{\mathrm r}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{C}\cong\mathbb{C}\oplus\mathbb{C}
$$
carries two binary conditions. The reduced norm $Q_+Q_-$ is zero or nonzero, and the two eigenvalues $Q_+$ and $Q_-$ are equal or distinct. The conditions are independent, so they cut the algebra into four **sectors**. In the idempotent coordinates $Q_\pm=Q_\blacktriangle\pm Q_\blacktriangledown$, with $\breve Q=Q_+\Pi_+ +Q_-\Pi_-$, the sectors are
$$
\Sigma_{11}=\{Q_+\neq0,\ Q_-\neq0,\ Q_+\neq Q_-\},\qquad
\Sigma_{01}=\{Q_+Q_-=0,\ Q_+\neq Q_-\},
$$
$$
\Sigma_{10}=\{Q_+=Q_-\neq0\},\qquad
\Sigma_{00}=\{Q_+=Q_-=0\}=\{0\}.
$$
The first index is the reduced norm ($1$ regular, $0$ degenerate), and the second is the spectrum ($1$ regular, $0$ degenerate). The article proves that all four are nonempty, describes each, computes its dimension and closure, and shows that no sector has a defective stratum. The spectral criterion is *Spectral Regularity and Degeneracy in the Reduced Biquaternion Algebra*; the comparison of the conditions is *Relations between the Reduced Norm and Spectral Regularity and Degeneracy*.

**Notation.** The element is $\breve Q=Q_\blacktriangle+jQ_\blacktriangledown$ with $j^{2}=+1$, $ij=ji$ and $i^{2}=-1$; $\Pi_\pm=\tfrac12(1\pm j)$; $Q_\pm=Q_\blacktriangle\pm Q_\blacktriangledown$; and $\breve Q=Q_+\Pi_+ +Q_-\Pi_-$. The algebra, the unit criterion and the zero divisors are *Reduced Biquaternion Space*, *Norm and Invertibility in the Algebra of the Reduced Biquaternions* and *Zero Divisors of the Algebra of the Reduced Biquaternions*.

## The Definition and the Partition

**Definition (the sectors).** For $i,j\in\{0,1\}$, the **sector** $\Sigma_{ij}$ is the set of elements whose reduced norm is nonzero exactly when $i=1$ and whose eigenvalues are distinct exactly when $j=1$. Explicitly, the four sectors are the four displays of the introduction.

**Theorem (the partition).** The sectors form a partition:
$$
\mathbb{B}_{\mathrm r}=\Sigma_{11}\sqcup\Sigma_{01}\sqcup\Sigma_{10}\sqcup\Sigma_{00}.
$$

*Proof.* Each element has one truth value for each binary predicate, so it lies in exactly one of the four combinations; the sets are disjoint and exhaustive.

**Theorem (all four are nonempty).** Each sector contains the element displayed in the table.

| sector | $(Q_+,Q_-)$ | element |
|---|---|---|
| $\Sigma_{11}$ | $(1,2)$ | $\tfrac32-\tfrac12 j$ |
| $\Sigma_{01}$ | $(0,1)$ | $\Pi_-$ |
| $\Sigma_{10}$ | $(1,1)$ | $1$ |
| $\Sigma_{00}$ | $(0,0)$ | $0$ |

*Proof.* The element is recovered from $(Q_+,Q_-)$ by $Q_\blacktriangle=\tfrac12(Q_++Q_-)$ and $Q_\blacktriangledown=\tfrac12(Q_+-Q_-)$, and the two conditions are read from the definitions; the table displays the four witnesses.

## The Sector $\Sigma_{11}$: The Open Dense Set

**Theorem (the generic sector).** The sector $\Sigma_{11}$ is the complement of the union of the three complex lines
$$
Q_+=0,\qquad Q_-=0,\qquad Q_+=Q_-.
$$
It is open and dense, connected, of complex dimension two and real dimension four. Its elements are units with distinct eigenvalues; each has a unique two-term spectral decomposition and the eigenbasis $(\Pi_+,\Pi_-)$.

*Proof.* The complement is open. The three lines are closed of real codimension two and empty interior, so the complement is dense and connected, the complement of a closed subset of real codimension at least two in a connected manifold being connected. The complex dimension is two because the algebra has complex dimension two and the removed set has complex dimension one. The elements are units because both idempotent coordinates are nonzero, and the eigenvalues are distinct by the second condition. The spectral decomposition and the eigenbasis are those of *Spectral Regularity and Degeneracy in the Reduced Biquaternion Algebra*, §*The Spectral Criterion* and §*The Eigenspaces*.

**Remark (generic but not closed under multiplication).** The complement of $\Sigma_{11}$ is a finite union of complex lines, so $\Sigma_{11}$ is the generic sector. It is not closed under multiplication: the factors $\tfrac32-\tfrac12 j$ and $\tfrac32+\tfrac12 j$ lie in $\Sigma_{11}$, and their product is the scalar $2$, which lies in $\Sigma_{10}$.

## The Sector $\Sigma_{01}$: The Two Punctured Hyperplanes

**Theorem (the zero divisors).** The sector $\Sigma_{01}$ is the union of the two punctured hyperplanes
$$
\Sigma_{01}=\mathbb{C}^{\times}\Pi_+\cup\mathbb{C}^{\times}\Pi_-,
\qquad
\mathbb{C}^{\times}\Pi_+=\{Q_-=0,\ Q_+\neq0\},
\quad
\mathbb{C}^{\times}\Pi_-=\{Q_+=0,\ Q_-\neq0\}.
$$
Each is a complex line minus the origin, of complex dimension one and real dimension two; the two components are disjoint, so the sector has two connected components. Its elements are zero divisors with distinct eigenvalues $\{0,\lambda\}$, $\lambda\neq0$; each has a unique two-term spectral decomposition with one zero eigenvalue. Its closure is
$$
\overline{\Sigma_{01}}=\{Q_+Q_-=0\}=\mathbb{C}\Pi_+\cup\mathbb{C}\Pi_-,
$$
the union of the two full lines, which contains the origin $\Sigma_{00}$.

*Proof.* The product $Q_+Q_-$ vanishes only when one factor vanishes. The condition $Q_+\neq Q_-$ excludes the origin, so exactly one factor is zero and the other is nonzero. If $Q_-=0$, then $\breve Q=Q_+\Pi_+$ with $Q_+\neq0$, which is $\mathbb{C}^{\times}\Pi_+$; if $Q_+=0$, then $\breve Q=Q_-\Pi_-$ with $Q_-\neq0$, which is $\mathbb{C}^{\times}\Pi_-$. The two lines meet only at the origin, which is excluded, so the components are disjoint. Each punctured line is homeomorphic to $\mathbb{C}^{\times}$ and is connected. The spectral decomposition is that of *Relations between the Reduced Norm and Spectral Regularity and Degeneracy*, §*The Zero Divisors Are Spectrally Regular*. The closure adds the origin to each line.

## The Sector $\Sigma_{10}$: The Punctured Central Line

**Theorem (the scalar units).** The sector $\Sigma_{10}$ is the punctured scalar line
$$
\Sigma_{10}=\mathbb{C}^{\times}\cdot1=\{Q_\blacktriangle\neq0,\ Q_\blacktriangledown=0\},
$$
of complex dimension one and real dimension two, and it is connected. Its elements are units with the repeated eigenvalue $Q_\blacktriangle$; the minimal polynomial is $X-Q_\blacktriangle$; the spectral decomposition is the one-term writing $Q_\blacktriangle1$; the eigenspace is all of $\mathbb{B}_{\mathrm r}$; and every element is semisimple, not defective. Its closure is the full scalar line
$$
\overline{\Sigma_{10}}=\mathbb{C}\cdot1=\{Q_+=Q_-\},
$$
which contains the origin $\Sigma_{00}$.

*Proof.* The conditions $Q_+=Q_-$ and $Q_+\neq0$ give $Q_\blacktriangle=Q_+\neq0$ and $Q_\blacktriangledown=0$. Conversely, a nonzero scalar has $Q_+=Q_-=Q_\blacktriangle\neq0$. The reduced norm is $Q_\blacktriangle^{2}\neq0$, so the element is a unit. The spectrum is the singleton $\{Q_\blacktriangle\}$, the characteristic polynomial is $(X-Q_\blacktriangle)^{2}$, and the minimal polynomial is $X-Q_\blacktriangle$, which is squarefree. The eigenspace is the whole algebra because $\breve Q=Q_\blacktriangle1$ acts as the scalar $Q_\blacktriangle$. The closure is the full line, the origin included.

**Remark (no Jordan part).** In the biquaternion algebra $\Sigma_{10}$ splits into a scalar line and a Jordan part; here the repeated eigenvalue forces the element to be scalar, so the Jordan part is empty.

## The Sector $\Sigma_{00}$: The Origin

**Theorem (the doubly degenerate point).** The sector $\Sigma_{00}$ is the singleton $\{0\}$, of complex dimension zero, and it is closed. It is the only element in both zero sets. Its spectrum is $\{0\}$, its characteristic polynomial is $X^{2}$, its minimal polynomial is $X$, its eigenspace is all of $\mathbb{B}_{\mathrm r}$, and its spectral decomposition is the one-term writing $0=0\cdot1$. It is the only nilpotent of the algebra, and it lies in the closure of every other sector.

*Proof.* The conditions $Q_+=Q_-=0$ give $Q_\blacktriangle=0$ and $Q_\blacktriangledown=0$, hence $\breve Q=0$; conversely $0$ satisfies both. The spectrum, the polynomials and the eigenspace are the scalar formulas at $Q_\blacktriangle=0$. If $\breve N^{k}=0$, then $N_+^{k}=0$ and $N_-^{k}=0$ in the field $\mathbb{C}$, so $N_+=N_-=0$; hence $0$ is the only nilpotent. The origin lies in the closure of $\Sigma_{11}$ because $\Sigma_{11}$ is dense, and in the closures of $\Sigma_{01}$ and $\Sigma_{10}$ by the two closure theorems.

## Dimensions and Closures

**Theorem (the dimensions).** The dimensions and descriptions are collected in the table; the first dimension is complex and the second is real.

| sector | condition | description | dimension |
|---|---|---|---|
| $\Sigma_{11}$ | $Q_+\neq0,\ Q_-\neq0,\ Q_+\neq Q_-$ | open dense set, units with distinct eigenvalues | $2$ complex, $4$ real |
| $\Sigma_{01}$ | $Q_+Q_-=0,\ Q_+\neq Q_-$ | two punctured hyperplanes, zero divisors with distinct eigenvalues | $1$ complex, $2$ real |
| $\Sigma_{10}$ | $Q_+=Q_-\neq0$ | punctured central line, scalar units | $1$ complex, $2$ real |
| $\Sigma_{00}$ | $Q_+=Q_-=0$ | the origin | $0$ complex, $0$ real |

**Theorem (the closures).** The closures are
$$
\overline{\Sigma_{11}}=\mathbb{B}_{\mathrm r},\qquad
\overline{\Sigma_{01}}=\Sigma_{01}\cup\Sigma_{00},\qquad
\overline{\Sigma_{10}}=\Sigma_{10}\cup\Sigma_{00},\qquad
\overline{\Sigma_{00}}=\Sigma_{00}.
$$

*Proof.* The complement of $\Sigma_{11}$ is the union of the three complex lines, a closed set with empty interior, so $\Sigma_{11}$ is dense and its closure is the whole algebra. The closure of a punctured complex line is the full line, which adds the origin; the closure of a union is the union of the closures. The origin is closed.

**Corollary (a stratification by sectors).** Each closure is a union of sectors, so the partition satisfies the frontier condition of a stratification. The sector $\Sigma_{11}$ is open and dense; the sectors $\Sigma_{01}$ and $\Sigma_{10}$ are locally closed; the sector $\Sigma_{00}$ is closed. The closures of the two mixed sectors meet at the origin.

*Proof.* The closure statements are the theorem. $\Sigma_{11}$ is open; $\Sigma_{01}=\{Q_+Q_-=0\}\cap\{Q_+\neq Q_-\}$ and $\Sigma_{10}=\{Q_+=Q_-\}\cap\{Q_+\neq0\}$ are locally closed; $\Sigma_{00}$ is closed. The frontier condition is the statement that each closure is a union of sectors.

## The Absence of a Defective Stratum

**Theorem (no defective element).** Every element of every sector is semisimple. There is no sector, and no subset of a sector, on which an element is defective.

*Proof.* On $\Sigma_{11}$ and $\Sigma_{01}$ the two eigenvalues are distinct, so the minimal polynomial is the product of two distinct linear factors, hence squarefree. On $\Sigma_{10}$ the element is scalar and the minimal polynomial is linear. On $\Sigma_{00}$ the element is zero and the minimal polynomial is $X$. In every case the minimal polynomial is squarefree, so the element is semisimple. A defective element would have a minimal polynomial with a repeated root, and none occurs.

**Remark (the comparison with the biquaternion algebra).** In the biquaternion algebra the minimal polynomial refines the sectors into six strata: $\Sigma_{10}$ splits into a scalar line and a Jordan part, and $\Sigma_{00}$ into the origin and the nonzero nilpotents. Those parts are empty here because $\mathbb{B}_{\mathrm r}\cong\mathbb{C}\times\mathbb{C}$ is reduced, while $M_2(\mathbb{C})$ is not: a nonzero nilpotent matrix exists in the matrix algebra, and no nonzero nilpotent exists in a product of fields.

## Summary

The reduced biquaternion algebra is partitioned into four sectors by the reduced norm $Q_+Q_-$ and the eigenvalue difference $Q_+-Q_-$:
$$
\Sigma_{11}=\{Q_+\neq0,Q_-\neq0,Q_+\neq Q_-\},\quad
\Sigma_{01}=\{Q_+Q_-=0,Q_+\neq Q_-\},
$$
$$
\Sigma_{10}=\{Q_+=Q_-\neq0\},\quad
\Sigma_{00}=\{Q_+=Q_-=0\}=\{0\}.
$$
All four are nonempty.

The generic sector $\Sigma_{11}$ is the complement of the three complex lines $Q_+=0$, $Q_-=0$ and $Q_+=Q_-$; it is open and dense, of complex dimension two, and consists of the units with distinct eigenvalues. The sector $\Sigma_{01}$ is the union of the two punctured hyperplanes $\mathbb{C}^{\times}\Pi_+$ and $\mathbb{C}^{\times}\Pi_-$, of complex dimension one, with two connected components; it consists of the zero divisors with distinct eigenvalues. The sector $\Sigma_{10}$ is the connected punctured scalar line $\mathbb{C}^{\times}\cdot1$, of complex dimension one; the sector $\Sigma_{00}$ is the origin.

The dimensions are $2,1,1,0$ over $\mathbb{C}$ and $4,2,2,0$ over $\mathbb{R}$. The closures are $\overline{\Sigma_{11}}=\mathbb{B}_{\mathrm r}$, $\overline{\Sigma_{01}}=\Sigma_{01}\cup\Sigma_{00}$, $\overline{\Sigma_{10}}=\Sigma_{10}\cup\Sigma_{00}$ and $\overline{\Sigma_{00}}=\Sigma_{00}$; the partition is a stratification.

No sector has a defective stratum. Every element is semisimple: the minimal polynomial is a product of distinct linear factors on $\Sigma_{11}$ and $\Sigma_{01}$, linear on $\Sigma_{10}$, and $X$ at the origin. The repeated-eigenvalue sector $\Sigma_{10}$ contains only scalars, and the only nilpotent is $0$. The defective cone and the Jordan parts of the biquaternion algebra are absent because $\mathbb{C}\times\mathbb{C}$ is reduced.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\Sigma_{11}$ | $Q_+\neq0$, $Q_-\neq0$, $Q_+\neq Q_-$: the open dense sector |
| $\Sigma_{01}$ | $Q_+Q_-=0$, $Q_+\neq Q_-$: the two punctured hyperplanes |
| $\Sigma_{10}$ | $Q_+=Q_-\neq0$: the punctured scalar line |
| $\Sigma_{00}$ | $Q_+=Q_-=0$: the origin |
| $\nu_0$ | $1$ if $Q_+Q_-\neq0$, $0$ otherwise |
| $\sigma_0$ | $1$ if $Q_+\neq Q_-$, $0$ otherwise |
| $\mathbb{C}^{\times}\Pi_\pm$ | the two punctured idempotent lines |
| $\mathbb{C}^{\times}\cdot1$ | the punctured scalar line |

## Further Reading

- [Spectral Regularity and Degeneracy in the Reduced Biquaternion Algebra](spectral-regularity-and-degeneracy-in-the-reduced-biquaternion-algebra.html), for the spectral criterion, the eigenspaces and the scalar stratum.
- [Relations between the Reduced Norm and Spectral Regularity and Degeneracy](relations-between-the-reduced-norm-and-spectral-regularity-and-degeneracy.html), for the independence of the two conditions and the chain of invariants.
- [Norm and Invertibility in the Algebra of the Reduced Biquaternions](norm-and-invertibility-in-the-general-plain-algebra-of-the-reduced-biquaternions.html), for the reduced norm and the unit criterion.
- [Zero Divisors of the Algebra of the Reduced Biquaternions](zero-divisors-of-the-general-plain-algebra-of-the-reduced-biquaternions.html), for the two punctured idempotent lines.
- [The Spectrum](spectral-regularity-and-degeneracy-in-the-biquaternion-algebra.html), for the defective cone and the Jordan strata that are absent here.
- [Relations between the N Norm and Spectral Regularity and Degeneracy](relations-between-quaternionic-norm-and-spectral-regularity-and-degeneracy.html), for the non-commutative four sectors and the refinement by the minimal polynomial.
