# __Relations between the Dual Norm and Spectral Degeneracy__

## Introduction

The dual-number algebra $\mathbb{D}'_R=R[\varepsilon]/(\varepsilon^2)$ carries two invariants that are easy to confuse because both are degenerate. The **norm** is $\langle Q\rangle=Q\bar Q=a^2$; it is multiplicative, of rank one, and it vanishes exactly on the maximal ideal $\mathrm{M}=\{a=0\}$. **Spectral degeneracy** is the repetition of the eigenvalue; for $Q=a+b\varepsilon$ the characteristic polynomial is $(X-a)^2$, so it holds for every element and carries no information at all. The informative companion of the norm is therefore not spectral degeneracy but **defect**, the failure of an eigenbasis: the minimal polynomial is $X-a$ on the real axis and $(X-a)^2$ off it, so the defective set is

$$
D=\{a+b\varepsilon : b\neq0\}=\mathbb{D}'_R\setminus R\cdot1.
$$

This article compares the norm and the defect. The comparison has a sharp answer. A unit can be defective: every $a+b\varepsilon$ with $a\neq0$ and $b\neq0$ is a unit and has minimal polynomial $(X-a)^2$. The only semisimple non-unit is the origin. Consequently the two invariants are independent only in the direction of the unit group: the combination "unit and defective" is open and dense, while the combination "non-unit and semisimple" is a single point. The sector table has three non-empty cells and one empty one when read on the non-zero elements, the empty cell being the origin. The chain of invariants runs from the element through the minimal polynomial and the characteristic polynomial to the norm, and each step forgets something: the minimal polynomial forgets the value of the infinitesimal part, the characteristic polynomial forgets the defect, and the norm forgets the sign of the eigenvalue.

**Notation and scope.** The algebra is $\mathbb{D}'_R$ over a real closed field $R$, with the geometric case $R=\mathbb{R}$; a general element is $Q=a+b\varepsilon$ with $a=\operatorname{Re}Q$ and $b=\operatorname{Inf}Q$, equal to $q+\varepsilon q'$ in the prime notation of *Dual-Numbers Algebra*. The norm is $\langle Q\rangle=Q\bar Q=a^2$, the conjugation is $\bar Q=a-b\varepsilon$, and $\mathrm{M}=(\varepsilon)=\{a=0\}$. The spectral theory is *Spectral Regularity and Degeneracy in the Dual-Number Algebra*, the defect is *The Defective Sector of the Dual-Number Algebra*, and the norm is *Dual-Numbers Norm and Invertibility*. The four sectors of the biquaternion algebra, used only for comparison at the end, are *Relations between Quaternionic Norm and Spectral Regularity and Degeneracy*.

**A word on the two tables.** The **norm/spectrum** table of article 1 has two empty cells, $\Sigma_{11}$ and $\Sigma_{01}$, because spectral regularity is impossible in $\mathbb{D}'_R$. The table of this article that has three non-empty cells and one empty one is the **norm/defect** table, not the norm/spectrum table. The two tables are distinguished in §*The Sector Tables*.

## The Norm

**The norm is a rank-one quadratic form whose radical is the maximal ideal; it is a function of the real part alone.**

**Definition (the norm).** The **norm** of $Q=a+b\varepsilon$ is

$$
\langle Q\rangle=Q\bar Q=(a+b\varepsilon)(a-b\varepsilon)=a^2.
$$

**Theorem (the properties of the norm).**

1. **Rank one.** The polar form is

$$
B(Q_1,Q_2)=\tfrac12\bigl(\langle Q_1+Q_2\rangle-\langle Q_1\rangle-\langle Q_2\rangle\bigr)=a_1a_2,
$$

of matrix $\begin{pmatrix}1&0\\0&0\end{pmatrix}$ in the basis $(1,\varepsilon)$; its radical is $\mathrm{M}$.

2. **Multiplicative.** $\langle Q_1Q_2\rangle=\langle Q_1\rangle\langle Q_2\rangle$.

3. **Vanishing locus.** Over the real closed field $R$, $\langle Q\rangle=0$ if and only if $a=0$, that is, if and only if $Q\in\mathrm{M}$.

4. **Unit criterion.** $Q$ is a unit if and only if $\langle Q\rangle\neq0$, that is, if and only if $a\neq0$.

*Proof.* (1) Expanding, $\langle Q_1+Q_2\rangle=(a_1+a_2)^2$, so the polar form is $a_1a_2$; the matrix has rank one and radical $\{a=0\}=\mathrm{M}$. (2) $Q_1Q_2=a_1a_2+(a_1b_2+b_1a_2)\varepsilon$, so the norm is $(a_1a_2)^2=a_1^2a_2^2$. (3) In a real closed field $a^2=0$ implies $a=0$. (4) The inverse formula $Q^{-1}=a^{-1}-a^{-2}b\varepsilon$ exists exactly when $a\neq0$.

**Corollary (the norm is blind to the infinitesimal part).** For every $Q$ and every $\eta\in\mathrm{M}$,

$$
\langle Q+\eta\rangle=\langle Q\rangle.
$$

*Proof.* Adding $\eta$ does not change the real part.

**Corollary (the norm is not a norm in the analytic sense).** It is homogeneous of degree two but degenerate, vanishing on the non-zero elements of $\mathrm{M}$; the positive-definite Euclidean form $a^2+b^2$ carries the topology but is not multiplicative.

*Proof.* Homogeneity and degeneracy are immediate from $a^2$. The failure of multiplicativity of the Euclidean form is *Dual-Numbers Norm and Invertibility*, §*The Euclidean Form*.

## The Defect

**The defect is the non-vanishing of the nilpotent part; unlike the norm, it is blind to the real part.**

**Definition (defect).** An element $Q$ is **defective** if its minimal polynomial has a repeated factor, equivalently if $L_Q$ is not diagonalisable, equivalently if it has no eigenbasis. The **defective set** is $D$.

**Theorem (the defect).** For $Q=a+b\varepsilon$,

$$
m_Q(X)=\begin{cases}X-a,&b=0,\\ (X-a)^2,&b\neq0,\end{cases}
\qquad
D=\{a+b\varepsilon : b\neq0\}=\mathbb{D}'_R\setminus R\cdot1.
$$

*Proof.* This is *The Defective Sector of the Dual-Number Algebra*, §*The Defective Set*: $Q-a=b\varepsilon$ has square zero and is non-zero exactly when $b\neq0$.

**Corollary (the defect is blind to the real part).** For every $a\in R$ and every non-zero $b$,

$$
a+b\varepsilon\in D.
$$

In particular the defective set contains the whole complement of the real axis, and not merely the punctured maximal ideal.

*Proof.* The minimal polynomial of $a+b\varepsilon$ is $(X-a)^2$ for every $a$ when $b\neq0$.

**Remark (the nilpotent part).** The projection $\nu(Q)=Q-\operatorname{Re}Q=b\varepsilon$ maps $D$ onto $\mathrm{M}\setminus\{0\}$; the defective set is the preimage of the punctured maximal ideal under $\nu$. Thus $\mathrm{M}\setminus\{0\}$ is the set of non-zero nilpotent parts, not the defective set. The defect is carried by the nilpotent part, exactly as the norm is carried by the real part.

**The two invariants side by side.**

| item | norm | defect |
|---|---|---|
| quantity | $a^2$ | the predicate $b\neq0$ |
| depends on | the real part $a$ | the infinitesimal part $b$ |
| zero set | $\mathrm{M}=\{a=0\}$ | the semisimple set $\{b=0\}$ |
| complement | the units $\{a\neq0\}$ | the defective set $\{b\neq0\}$ |
| multiplicative | yes | no |
| role | the invertibility criterion | the eigenbasis criterion |

## The Implications

**The two predicates point in opposite directions, and their interaction is exhausted by three statements.**

**Theorem (the implications).**

1. If $Q\neq0$ and $\langle Q\rangle=0$, then $Q$ is defective.
2. If $Q\neq0$ and $Q$ is semisimple, then $\langle Q\rangle\neq0$.
3. Every $a+b\varepsilon$ with $a\neq0$ and $b\neq0$ is a defective unit; in particular $1+\varepsilon$ is.
4. The only semisimple non-unit is the origin.

*Proof.* (1) $\langle Q\rangle=0$ gives $a=0$, and $Q\neq0$ then gives $Q=b\varepsilon$ with $b\neq0$; the minimal polynomial is $X^2$, which is repeated. (2) Semisimple gives $b=0$, so $Q=a$; $Q\neq0$ gives $a\neq0$, and $a^2\neq0$. (3) The unit criterion gives the unit, and the minimal polynomial $(X-a)^2$ gives the defect; $1+\varepsilon$ is the case $a=b=1$. (4) Semisimple gives $Q=a$; a non-unit has $a=0$, hence $Q=0$.

**Corollary (the witness table).**

| | semisimple | defective |
|---|---|---|
| **unit** | $1$ | $1+\varepsilon$ |
| **non-unit** | $0$ | $\varepsilon$ |

The four elements have the data

| element | norm | minimal polynomial | unit | defect |
|---|---|---|---|---|
| $1$ | $1$ | $X-1$ | yes | no |
| $1+\varepsilon$ | $1$ | $(X-1)^2$ | yes | yes |
| $\varepsilon$ | $0$ | $X^2$ | no | yes |
| $0$ | $0$ | $X$ | no | no |

*Proof.* The norms are $1,1,0,0$; the minimal polynomials are those of the table; the unit criterion is $a\neq0$; the defect criterion is $b\neq0$.

**Theorem (the only direction of independence).** On the non-zero elements, the norm and the defect are independent only on the norm-regular side. Precisely: the combination "norm-degenerate and semisimple" is empty away from the origin, while the combination "norm-regular and defective" is the open dense set

$$
D_1=\{a+b\varepsilon : a\neq0,\ b\neq0\}.
$$

The other two combinations, "norm-regular and semisimple" and "norm-degenerate and defective", are the punctured real axis $R^\times$ and the punctured maximal ideal $\mathrm{M}\setminus\{0\}$.

*Proof.* The four combinations are the intersections of $\{a\neq0\}$ or $\{a=0\}$ with $\{b=0\}$ or $\{b\neq0\}$; they are $R^\times$, $D_1$, $\{0\}$ and $\mathrm{M}\setminus\{0\}$. The second is open and dense because it is the complement of the two axes; the third is the origin.

So the algebra is the disjoint union of four sets,

$$
\mathbb{D}'_R=R^\times\ \sqcup\ D_1\ \sqcup\ (\mathrm{M}\setminus\{0\})\ \sqcup\ \{0\},
$$

and the two invariants are the two coordinates of this decomposition: the norm decides between the first two sets and the last two, and the defect decides between the first and third and the second and fourth. The norm and the defect are not functions of one another: $1$ and $1+\varepsilon$ have the same norm and different defect; $\varepsilon$ and $1+\varepsilon$ have the same defect and different norm. They are both functions of the minimal polynomial, and the minimal polynomial is their common refinement.

## The Sector Tables

**The norm/spectrum table has two empty cells; the norm/defect table has three non-empty cells and one empty one on the non-zero elements.**

**Definition (the norm/spectrum sectors).** For $i,j\in\{0,1\}$, the sector $\Sigma_{ij}$ is the set of elements with $\langle Q\rangle\neq0$ if $i=1$ and $\langle Q\rangle=0$ if $i=0$, and with $Q$ spectrally regular if $j=1$ and spectrally degenerate if $j=0$.

**Theorem (the norm/spectrum table).** In $\mathbb{D}'_R$,

$$
\Sigma_{11}=\varnothing,\qquad
\Sigma_{01}=\varnothing,\qquad
\Sigma_{10}=\{a\neq0\}=(\mathbb{D}'_R)^\times,\qquad
\Sigma_{00}=\mathrm{M}=\{a=0\}.
$$

*Proof.* Spectral regularity is impossible by *Spectral Regularity and Degeneracy in the Dual-Number Algebra*, §*The Theorem: Universal Spectral Degeneracy*; the remaining two sectors are the unit criterion and its complement.

| norm/spectrum | spectrally regular | spectrally degenerate |
|---|---|---|
| **norm-regular** | $\Sigma_{11}=\varnothing$ | $\Sigma_{10}=\{a\neq0\}$ |
| **norm-degenerate** | $\Sigma_{01}=\varnothing$ | $\Sigma_{00}=\mathrm{M}$ |

**Definition (the norm/defect sectors).** For $i,j\in\{0,1\}$, let $T_{ij}$ be the set of elements with the norm condition indexed by $i$ and with $Q$ semisimple if $j=1$ and defective if $j=0$.

**Theorem (the norm/defect table).**

$$
T_{11}=R^\times,\qquad
T_{10}=D_1=\{a\neq0,\ b\neq0\},\qquad
T_{01}=\{0\},\qquad
T_{00}=\mathrm{M}\setminus\{0\}.
$$

*Proof.* The four sets are the intersections of the two axes and their complements, computed in §*The Implications*.

| norm/defect | semisimple | defective |
|---|---|---|
| **norm-regular** | $T_{11}=R^\times$ | $T_{10}=D_1$ |
| **norm-degenerate** | $T_{01}=\{0\}$ | $T_{00}=\mathrm{M}\setminus\{0\}$ |

**Corollary (the count).** The norm/defect table has four non-empty cells if the origin is counted, and three non-empty cells and one empty one when it is read on the non-zero elements. The empty cell is $T_{01}=\{0\}$, the single semisimple non-unit. The three non-empty cells are the punctured real axis, the open dense set of defective units, and the punctured maximal ideal. The norm/spectrum table, by contrast, has two non-empty cells and two empty ones.

*Proof.* The identifications are the theorem; the only cell that disappears on removing the origin is $T_{01}$.

**Remark (the refinement).** The norm/defect table refines the norm/spectrum table:

$$
\Sigma_{10}=T_{11}\sqcup T_{10},\qquad
\Sigma_{00}=T_{01}\sqcup T_{00}.
$$

The norm/spectrum table collapses the defect distinction inside the units and inside the maximal ideal. The norm/defect table keeps it, and it is the table in which the three non-empty cells and the empty one are visible.

## The Chain of Invariants

**The element determines its minimal polynomial, the minimal polynomial determines the characteristic polynomial, and the characteristic polynomial determines the norm; each arrow loses information: the value of $b$ is lost at the first, the defect at the second, and the sign of $a$ at the third.**

**Theorem (the chain).** For every $Q=a+b\varepsilon$,

$$
(a,b)\ \longmapsto\ m_Q\ \longmapsto\ p_Q\ \longmapsto\ \langle Q\rangle,
$$

with

$$
p_Q(X)=m_Q(X)^2\ \text{if } b=0,\qquad
p_Q(X)=m_Q(X)\ \text{if } b\neq0,
\qquad
p_Q(X)=(X-a)^2,
\qquad
\langle Q\rangle=a^2.
$$

In particular the norm is the constant term of the characteristic polynomial, and the characteristic polynomial has only one independent coefficient:

$$
p_Q(X)=\Bigl(X-\frac{\operatorname{tr}L_Q}{2}\Bigr)^2,
\qquad
\langle Q\rangle=\Bigl(\frac{\operatorname{tr}L_Q}{2}\Bigr)^2.
$$

*Proof.* The minimal polynomial is the dichotomy of §*The Defect*; the characteristic polynomial is $(X-a)^2$. If $b=0$, then $m_Q=X-a$ and $m_Q^2=(X-a)^2=p_Q$; if $b\neq0$, then $m_Q=(X-a)^2=p_Q$. The trace is $2a$, and the constant term is $a^2$.

**The chain of information.**

| invariant | value | degeneration patterns | what it sees |
|---|---|---|---|
| norm | $a^2$ | $2$ | whether the eigenvalue is zero |
| characteristic polynomial | $(X-a)^2$, equivalently $2a$ | $2$ | the eigenvalue $a$, including its sign |
| minimal polynomial | $X-a$ or $(X-a)^2$ | $4$ | the eigenvalue and the defect |
| Jordan type | $aI$ or $J_2(a)$ | $4$ | the eigenvalue and the defect, up to conjugacy |
| element | $(a,b)$ | — | the eigenvalue and the value of $b$ |

The count of patterns is the count of degeneration types, not of values: the characteristic polynomial and the minimal polynomial take infinitely many values, and the table counts the patterns into which those values fall.

*Proof.* The norm has two patterns, zero and non-zero. The characteristic polynomial is always a square, and the square is at zero or away from zero; its value records $a$. The minimal polynomial has the four patterns $X$, $X-a$ with $a\neq0$, $X^2$, and $(X-a)^2$ with $a\neq0$. The Jordan type has the four patterns $0$, $aI$ with $a\neq0$, $J_2(0)$ and $J_2(a)$ with $a\neq0$. The element is the pair $(a,b)$.

**Corollary (the minimal polynomial is the first invariant that sees the defect).** The norm and the characteristic polynomial depend only on $a$, so $a$ and $a+b\varepsilon$ have the same norm and the same characteristic polynomial. The minimal polynomial distinguishes them, $X-a$ against $(X-a)^2$.

*Proof.* The norm and the characteristic polynomial depend only on $a$; the minimal polynomial depends on $a$ and on whether $b=0$.

## Summary

The norm is $\langle Q\rangle=a^2$, a degenerate quadratic form of rank one, multiplicative, with radical $\mathrm{M}$, non-zero exactly on the units and blind to the infinitesimal part. The defect is the failure of an eigenbasis, decided by the minimal polynomial; the defective set is $D=\{b\neq0\}=\mathbb{D}'\setminus R\cdot1$, blind to the real part and carried by the nilpotent part $b\varepsilon\in\mathrm{M}$. The punctured maximal ideal is the nilpotent stratum, not the whole defective set.

The interaction is exhausted by four statements: a non-zero norm-degenerate element is defective; a non-zero semisimple element is a unit; a unit can be defective ($1+\varepsilon$ is the simplest witness); and the only semisimple non-unit is the origin. Hence $\mathbb{D}'=R^\times\sqcup D_1\sqcup(\mathrm{M}\setminus\{0\})\sqcup\{0\}$. The norm/spectrum table has two empty cells, $\Sigma_{11}$ and $\Sigma_{01}$, and two non-empty cells, $\Sigma_{10}$ and $\Sigma_{00}$. The norm/defect table has $T_{11}=R^\times$, $T_{10}=D_1$, $T_{01}=\{0\}$, $T_{00}=\mathrm{M}\setminus\{0\}$; on the non-zero elements it has three non-empty cells and one empty one, the empty cell being the origin.

The chain is $(a,b)\mapsto m_Q\mapsto p_Q\mapsto\langle Q\rangle$. The minimal polynomial fixes the eigenvalue and the defect bit but not $b$; the characteristic polynomial is $(X-a)^2$ in both defect cases, so it loses the defect, and it has one independent coefficient because the norm is the square of half the trace; the norm loses the sign of the eigenvalue. The minimal polynomial is the first invariant that sees the defect, and the norm is the last that still sees the eigenvalue, up to sign.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\mathbb{D}'_R=R[\varepsilon]/(\varepsilon^2)$ | the dual-number algebra over $R$ |
| $Q=a+b\varepsilon$ | a general element, equal to $q+\varepsilon q'$ in the prime notation |
| $a=\operatorname{Re}Q$, $b=\operatorname{Inf}Q$ | real and infinitesimal parts |
| $\langle Q\rangle=Q\bar Q=a^2$ | the norm, the dual norm |
| $B(Q_1,Q_2)=a_1a_2$ | the polar form of the norm |
| $\mathrm{M}=(\varepsilon)=\{a=0\}$ | the maximal ideal, the radical of the norm |
| $m_Q$ | the minimal polynomial: $X-a$ if $b=0$, $(X-a)^2$ if $b\neq0$ |
| $D=\{b\neq0\}$ | the defective set |
| $D_1=\{a\neq0,b\neq0\}$ | the defective units |
| $\mathrm{M}\setminus\{0\}=\{a=0,b\neq0\}$ | the nilpotent stratum |
| $R^\times=\{a\neq0,b=0\}$ | the nonzero real scalars, the semisimple units |
| $\{0\}$ | the unique semisimple non-unit |
| $\Sigma_{ij}$ | the norm/spectrum sectors: $i$ for the norm, $j$ for spectral regularity |
| $T_{ij}$ | the norm/defect sectors: $i$ for the norm, $j$ for semisimplicity |
| $p_Q(X)=(X-a)^2$ | the characteristic polynomial |
| $\operatorname{tr}L_Q=2a$ | the trace; $\langle Q\rangle=(\operatorname{tr}L_Q/2)^2$ |
| $J_2(a)$ | the Jordan block of the defective sector |

## Further Reading

- [Dual-Numbers Algebra](dual-numbers-algebra.html), for the algebra, the maximal ideal and the two conjugations.
- [Dual-Numbers Norm and Invertibility](dual-numbers-norm-and-invertibility.html), for the norm, its rank, its radical and the unit criterion.
- [Dual-Numbers Zero Divisors](dual-numbers-zero-divisors.html), for the nilpotent stratum and the zero-divisor set.
- [The Defective Sector of the Dual-Number Algebra](the-defective-sector-of-the-dual-number-algebra.html), for the defect, its two strata and the module picture.
- [Spectral Regularity and Degeneracy in the Dual-Number Algebra](spectral-regularity-and-degeneracy-in-the-dual-number-algebra.html), for the characteristic polynomial, the universal degeneracy and the norm/spectrum sectors.
- [Relations between Quaternionic Norm and Spectral Regularity and Degeneracy](relations-between-quaternionic-norm-and-spectral-regularity-and-degeneracy.html), for the four sectors and the chain of invariants in the biquaternion algebra.
- [Spectral Regularity and Degeneracy in the Biquaternion Algebra](spectral-regularity-and-degeneracy-in-the-biquaternion-algebra.html), for the defect on the biquaternion spectral-degenerate cone.
- [Nilpotent Elements and the Jordan–Chevalley Decomposition](nilpotent-elements-and-the-jordan-chevalley-decomposition.html), for semisimplicity and the additive decomposition.
- [Modules over $k[x]$ and the Jordan Form](modules-over-kx-and-the-jordan-form.html), for the Jordan type and the module picture.
- [Dual-Numbers Matrix Element Representation](dual-numbers-matrix-element-representation.html), for the matrix model and the determinant as the norm.
- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (2nd edition, Cambridge University Press, 2013), for the trace, the determinant and the characteristic polynomial.
- T. Y. Lam, *Introduction to Quadratic Forms over Fields* (American Mathematical Society, Providence, 2005), for degenerate quadratic forms and their radicals.
- Michael F. Atiyah and Ian G. Macdonald, *Introduction to Commutative Algebra* (Addison-Wesley, Reading, 1969), for local rings and nilpotent ideals.
